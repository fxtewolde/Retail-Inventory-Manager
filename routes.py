from flask import Flask, render_template, redirect, url_for, request
from models import locations
from functools import reduce
import sqlite3  # Make sure to import sqlite3
import os

# Should we perhaps connect to the database in the global space and just maintain a single cursor
# for all routes?
# We might want to use a singleton or a factory here.

def register_routes(app, db):
    @app.route('/')
    def index():
        loc = locations.query.all()  # Get all locations from the database
        return render_template('index.html', loc=loc)
    
    @app.route('/q')
    def query_db():
        column_names_list, results_list = execute_sql_from_file('./querys.sql')
        queries_data = zip(column_names_list, results_list)  
        return render_template('queries.html', queries_data=queries_data)

    # CODE NOTES:
    # The inventory template in the frontend is set up so that when a user selects a store from the dropdown
    # The app will send a GET request for the store inventory, and a list of products that can be added to a store's inventory
    # In detail, the queries are:
    # 1. Get the location data for the dropdown menu so that a user can switch stores.
    # 2. Get the current location's current inventory
    # 3. Query the products table for all products that are not in the current inventory (ie. a Subraction query).

    # On a POST request, the user can either set a product on backorder or update the quantity.
    # Depending on which request is posted, it'll send the appropriate data and we check for None to determine which data to update.
    # If we're updating quantity, we run the update quantity query
    # If we're updating backorder, we run the update backorder query
    # If we're adding a product (from the add applet at the bottom), we insert into the table.
    # We then finish by committing to the database and redirect the user with another GET request.
    @app.route('/inventory', methods=['GET', 'POST'])
    def inventory():
        if request.method == 'POST':
            l_id = request.form.get('location_id', None)
            p_id = request.form.get('product_id', None)

            new_quantity = request.form.get('new_quantity', None)
            on_backorder = request.form.get('on_backorder', None)

            # This is just so that we have a functioning toggle.
            off_backorder = request.form.get('off_backorder', None)

            add_quantity = request.form.get('add_quantity', None)

            
            # We escape early to prevent integrity problems.
            if l_id is None or p_id is None:
                return redirect(url_for('inventory', location_id=None))



            conn = sqlite3.connect('instance/database.db')
            if new_quantity is not None:
                quan_cur = conn.cursor()
                quan_cur.execute("""UPDATE inventory SET quantity = ?
                             WHERE location_id = ? AND product_id = ?""", [new_quantity, l_id, p_id])

            if on_backorder is not None or off_backorder is not None:
                on_backorder = 1 if on_backorder == "on" else 0 
                bo_cur = conn.cursor()
                bo_cur.execute("""UPDATE inventory SET on_backorder = ?
                             WHERE location_id = ? AND product_id = ?""", [on_backorder, l_id, p_id])

            if add_quantity is not None:
                add_cur = conn.cursor()
                # Weird: Query won't use default value constraint -> not sure why.
                add_cur.execute("""INSERT INTO inventory (location_id, product_id, quantity, on_backorder)
                                VALUES (?, ?, ?, ?)""", [l_id, p_id, add_quantity, 0])


            conn.commit()
            return redirect(url_for('inventory', location_id=l_id))



        else:
            # Get a cursor
            conn = sqlite3.connect('instance/database.db')
            loc_cur = conn.cursor()

            # Check location ID for custom inventory page
            location_id = request.args.get('location_id')

            # Get the location addresses/ids
            location_data = loc_cur.execute("""SELECT id, 
                                        id || ': ' || street_address || ', ' || suite_no || ', ' || city || ', ' || province as address
                                                     FROM locations""")

            # If there's no location selected (eg. opening the inventory app)
            # Return with the location data; user can pick a location in the inventory app.
            if location_id is None or location_id == '':
                return render_template('inventory.html', location_data=location_data)
           
            # VIEWING INVENTORY
            # Get an inventory cursor
            inv_cur = conn.cursor()
            # Get the query data 
            inventory_data = inv_cur.execute("""SELECT i.product_id as 'ID', 
                                                    pd.product_name as 'Product Name', 
                                                    p.retail_price as 'Retail Price', 
                                                    i.quantity as 'Quantity',
                                                    CASE
                                                        WHEN i.on_backorder = 1 THEN 'TRUE'
                                                        WHEN i.on_backorder = 0 THEN 'FALSE'
                                                        ELSE 'N/A'
                                                    END as 'On Backorder'
                                                 FROM inventory i
                                                 JOIN products p on i.product_id = p.id
                                                 JOIN product_details pd on pd.upc_a = p.upc_a
                                                 WHERE i.location_id = ?""", [location_id])
            # Get the column names from the query data
            column_names = [column[0] for column in inventory_data.description][1:]

            # ADDING PRODUCTS
            # Get another cursor
            add_cur = conn.cursor()
            available_products = add_cur.execute("""SELECT p.id as 'ID', 
                                                        pd.product_name as 'Product Name', 
                                                        p.retail_price as 'Retail Price' 
                                                    FROM products p
                                                    JOIN product_details pd on pd.upc_a = p.upc_a
                                                    WHERE p.id NOT IN (SELECT product_id
                                                                       FROM inventory
                                                                       WHERE location_id = ?)""", [location_id])
            available_columns = [column[0] for column in available_products.description][1:]

            return render_template('inventory.html', current_location=int(location_id), location_data=location_data, column_names=column_names, inventory_data=inventory_data, available_products=available_products, available_columns=available_columns)
   
    # CODE NOTES:  This one is a little bit complicated. In the frontend, we have a 3-part conditional render.
    # If a basic GET request is sent, the user is served the search tool to find optimum account holders.
    # Our search tool will do an ID lookup if we send the optimum ID via POST request and it will return 0-1 users in a list
    # When we send the 1-tuple list to the frontend, it will unpack the tuple and render the relevant data.
    
    # If the user searches by any other data in the POST request, we do a partial string search to find a list of potential optimum matches.
    # When this is served to the frontend, the tuples are unpacked to show names + optimum id number.
    # The app user can click on any of the rows they wish to see in detail and the frontend will send a POST request with the optimum ID -> this then performs the above ID query.
    
    # At the moment, our fuzzy search isn't particularly efficient. We have an order of precedence as you see in the frontend; First Name, Last Name ... etc.
    # The router will just pick whichever one it finds first and we do not yet support multiple-data in the query.
    # We need to figure out how to handle the empty string + wildcard situation; We cannot OR them, or we pick up all records in the database.

    @app.route('/optimum', methods=['GET', 'POST'])
    def optimum():
        if request.method == 'POST':
            o_id = request.form.get('optimum_id', None)
            o_first_name = request.form.get('first_name', None)
            o_last_name = request.form.get('last_name', None)
            o_telephone = request.form.get('telephone', None)
            o_email = request.form.get('email', None)
            
            # Connect to the database
            conn = sqlite3.connect('instance/database.db')
            # search by optimum number -> return the record.

            if o_id is not None and o_id != '':
                cur = conn.cursor()
                op_member = cur.execute("""SELECT o.id as 'Member #', c.first_name || ' ' || c.last_name as 'Member', o.optimum_points as 'Points'
                                           FROM optimum_members o
                                           JOIN customers c ON c.id = o.customer_id
                                           WHERE o.id = ?""", [o_id])


                cols = [column[0] for column in op_member.description]

                # Get the column names
                return render_template('optimum.html', optimum_member=op_member, columns=cols)

            # Search by customer data -> return a list of records.
            # There is likely a way to do this way more elegantly, but we are crunched for time.
            if o_first_name and o_first_name != ' ':
                cur = conn.cursor()
                op_members = cur.execute("""SELECT o.id as 'Member #', c.first_name || ' ' || c.last_name as 'Member'
                                            FROM optimum_members o
                                            JOIN customers c ON c.id = o.customer_id
                                            WHERE c.first_name LIKE ? 
                                                    """, ['%'+o_first_name+'%'])


                cols = [column[0] for column in op_members.description]

                return render_template('optimum.html', optimum_members=op_members, columns=cols)


            if o_last_name and o_last_name != ' ':
                cur = conn.cursor()
                op_members = cur.execute("""SELECT o.id as 'Member #', c.first_name || ' ' || c.last_name as 'Member'
                                            FROM optimum_members o
                                            JOIN customers c ON c.id = o.customer_id
                                            WHERE c.last_name LIKE ? 
                                                    """, ['%'+o_last_name+'%'])


                cols = [column[0] for column in op_members.description]

                return render_template('optimum.html', optimum_members=op_members, columns=cols)


            if o_telephone and o_telephone != ' ':
                cur = conn.cursor()
                op_members = cur.execute("""SELECT o.id as 'Member #', c.first_name || ' ' || c.last_name as 'Member'
                                            FROM optimum_members o
                                            JOIN customers c ON c.id = o.customer_id
                                            WHERE c.telephone LIKE ? 
                                                    """, ['%'+o_telephone+'%'])


                cols = [column[0] for column in op_members.description]

                return render_template('optimum.html', optimum_members=op_members, columns=cols)


            if o_email and o_email != ' ':
                cur = conn.cursor()
                op_members = cur.execute("""SELECT o.id as 'Member #', c.first_name || ' ' || c.last_name as 'Member'
                                            FROM optimum_members o
                                            JOIN customers c ON c.id = o.customer_id
                                            WHERE c.email LIKE ? 
                                                    """, ['%'+o_email+'%'])


                cols = [column[0] for column in op_members.description]

                return render_template('optimum.html', optimum_members=op_members, columns=cols)

            # If the post-request fails, clear and return to search page
            return redirect(url_for('optimum'))

        else:
            # Search page
            return render_template('optimum.html')



    @app.route('/p')
    def populate_db():
        run_sql_script('./populate_tables.sql')  
        return "Tables populated successfully!"
    
    @app.route('/d')
    def drop_db():
        run_sql_script('./drop_tables.sql')  
        return "Tables dropped successfully!"
    
    @app.route('/c')
    def create_db():
        with app.app_context():  
            db.create_all()  
        return "Tables created successfully!"
   
    ## Werkzeug.server? -> This doesn't seem to be working.
    @app.route('/exit', methods=['GET'])
    def exit_app():
        """Terminate the Flask server."""
        shutdown = request.environ.get('werkzeug.server.shutdown')
        if shutdown is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        shutdown()
        return "Server shutting down..."
        

def run_sql_script(sql_file):
    # Connect to the database
    try:
        connection = sqlite3.connect('instance/database.db')  # Ensure the path matches your database
        cursor = connection.cursor()

        # Read the SQL file
        with open(sql_file, 'r') as f:
            sql_script = f.read()

        # Execute the SQL script
        cursor.executescript(sql_script)
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error executing SQL script: {e}")
        raise  # Re-raise the exception after logging it



def execute_sql_from_file(sql_file):
    """Execute multiple SQL queries from a file and return their results."""
    connection = sqlite3.connect('instance/database.db')  # Ensure the path matches your DB
    cursor = connection.cursor()
    
    results = []
    column_names = []

    try:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        
        # Split the script into individual statements
        queries = sql_script.split(";")
        for query in queries:
            query = query.strip()  # Remove leading/trailing whitespace
            if query:  # Skip empty statements
                cursor.execute(query)
                if cursor.description:  # If the query returns results
                    column_names.append([desc[0] for desc in cursor.description])
                    results.append(cursor.fetchall())
        connection.commit()
    except Exception as e:
        print(f"Error executing SQL: {e}")
        raise
    finally:
        connection.close()
    
    return column_names, results
