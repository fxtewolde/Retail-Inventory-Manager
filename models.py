from app import db
from datetime import datetime

class locations(db.Model):
	__tablename__ = 'locations'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	street_address = db.Column(db.String(255), default='street', nullable= False)
	suite_no = db.Column(db.Integer, default= 0, nullable= False)
	city = db.Column(db.String(100), default= 'city', nullable= False)
	province = db.Column(db.String(100), default= 'province', nullable= False)
	postal_code = db.Column(db.String(6), default= 'A1A2C3', nullable= False)
	pharmacy_owner = db.Column(db.String(100), default= 'owner', nullable= False)
	def __repr__(self):
		return f'Shoppers {self.id} is located at {self.street_address}, {self.city}, {self.province}'

class departments(db.Model):
	__tablename__ = 'departments'
	id = db.Column(db.Integer, default = 0, primary_key=True)
	department_name = db.Column(db.String(100), default= 'department', nullable= False)
	def __repr__(self):
		return f'Shoppers has {self.department_name} with id {self.id}'

class employees(db.Model):
	__tablename__ = 'employees'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	first_name = db.Column(db.String(100), default= 'name', nullable= False)
	last_name = db.Column(db.String(100), default= 'name', nullable= False)
	telephone = db.Column(db.String(15), default= '1-555-555-5555', nullable= False)
	employee_password = db.Column(db.String(60), default='0', nullable=False)
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id', ondelete='SET NULL'))
	location_id = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete='SET NULL'))
	supervisor_id = db.Column(db.Integer, db.ForeignKey('employees.id', ondelete='SET NULL'), nullable=True)
	payroll_id = db.Column(db.Integer, default= 0, unique=True, nullable=False)
	def __repr__(self):
		return f'Shoppers {self.location_id} has a employee: {self.id}, {self.first_name}, {self.last_name}'
	
class customers(db.Model):
	__tablename__ = 'customers'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	first_name = db.Column(db.String(100), default= 'name', nullable= False)
	last_name = db.Column(db.String(100), default= 'name', nullable= False)
	telephone = db.Column(db.String(15), default= '1-555-555-5555', nullable= False)
	email = db.Column(db.String(100), default= 'email@example.com',  nullable= False)
	__table_args__ = (
        db.CheckConstraint("email LIKE '%_@_%._%'"),
    )
	def __repr__(self):
		return f'Shoppers has a customer: {self.id}, {self.first_name}, {self.last_name}'
	

class optimum_members(db.Model):
	__tablename__ = 'optimum_members'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	optimum_points = db.Column(db.Integer, default=0, nullable=False)
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
	def __repr__(self):
		return f'Customer {self.customer_id} has a {self.optimum_points} points'
	
class suppliers(db.Model):
	__tablename__ ='suppliers'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	supplier_name = db.Column(db.String(100), default= 'name', unique=True, nullable= False)
	telephone = db.Column(db.String(15), default= '1-555-555-5555', nullable= False)
	email = db.Column(db.String(100), default= 'email@example.com', nullable= False)
	credit_owing = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	total_owing = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	__table_args__ = (
        db.CheckConstraint("email LIKE '%_@_%._%'"),
    )

class product_details(db.Model):
	__tablename__= 'product_details'
	upc_a = db.Column(db.String(15), default= "0-00000-00000-0", primary_key=True)
	product_name = db.Column(db.String(100), default= "name", nullable=False)
	category = db.Column(db.String(100), default ="no category", nullable=False)
	details = db.Column(db.String(3000), nullable=True)



class products(db.Model):
	__tablename__= 'products'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	upc_a = db.Column(db.String(15), db.ForeignKey('product_details.upc_a'), nullable=False)
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id', ondelete='SET NULL'))
	supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
	retail_price = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	unit_price = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)

class medications(db.Model):
	__tablename__ = 'medications'
	drug_indentification_number = db.Column(db.String(8), default= "00000000", primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='SET NULL'), default= 0)

class patients(db.Model):
	__tablename__= 'patients'
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), default= 0,primary_key=True)
	spouse_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), default= 0)
	parent_1_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), default= 0)
	parent_2_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), default= 0)

class prescriptions(db.Model):
	__tablename__= 'prescriptions'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('patients.customer_id', ondelete='CASCADE'), default= 0, primary_key=True)
	drug_indentification_number = db.Column(db.String(8), db.ForeignKey('medications.drug_indentification_number', ondelete='CASCADE'), default= "00000000")
	practitioner_mnic = db.Column(db.String(14), default= "CAMD-1234-5678" , nullable=False)


class transactions(db.Model):
	__tablename__='transactions'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	employee_id = db.Column(db.Integer, db.ForeignKey('employees.id', ondelete='SET NULL'), nullable=True)
	location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)  # Should not default to 0
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), nullable=True)

	subtotal = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	transaction_date = db.Column(db.DateTime(timezone=True), default= datetime.utcnow, nullable=False)

class orders(db.Model): 
	__tablename__='orders'
	id = db.Column(db.Integer, default= 0, primary_key=True)
	placed_on = db.Column(db.DateTime(timezone=True), default= datetime.utcnow, nullable=False)
	expected_on = db.Column(db.DateTime(timezone=True), default= datetime.utcnow, nullable=False)
	received_on = db.Column(db.DateTime(timezone=True), nullable=True)

class order_details(db.Model):
	__tablename__= 'order_details'
	order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
	quantity = db.Column(db.Integer, default= 0, nullable= False)
	__table_args__ = (
        db.PrimaryKeyConstraint('order_id', 'product_id'),
    )

class insurance(db.Model):
	__tablename__='insurance'
	policy_id = db.Column(db.String(100), primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('patients.customer_id', ondelete='SET NULL'), nullable=False)
	company_name = db.Column(db.String(100), default='company', nullable=False)

class filled_prescriptions(db.Model):
	__tablename__= 'filled_prescriptions'
	precription_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id', ondelete='CASCADE'), nullable=False)
	fill_date = db.Column(db.DateTime(timezone=True), nullable=False)
	__table_args__ = (
        db.PrimaryKeyConstraint('precription_id', 'fill_date'),
    )

class inventory(db.Model):
	__tablename__='inventory'
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), default= 0, nullable=False)
	location_id = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete='CASCADE'), default= 0, nullable=False)
	quantity = db.Column(db.Integer, default=0, nullable=False)
	on_backorder = db.Column(db.Integer, default=0, nullable=False)
	__table_args__ = (
        db.PrimaryKeyConstraint('product_id', 'location_id', name='inventory_id'),
        db.CheckConstraint("on_backorder IN (0, 1)", name="check_on_backorder"),

    )

class product_sales(db.Model):
	__tablename__= 'product_sales'
	transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id', ondelete="CASCADE"),default= 0)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), default= 0, nullable=False)
	discount = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	tax_rate = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	quantity = db.Column(db.Integer, default=0, nullable=False)
	__table_args__ = (
        db.PrimaryKeyConstraint('transaction_id', 'product_id', name='sales_id'),
    )

class payments(db.Model):
	__tablename__ ='payments'
	transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id', ondelete="CASCADE"), default= 0)
	method_of_payment = db.Column(db.String(15), default='cash', nullable=False)
	total_paid = db.Column(db.Numeric(19, 4), default=0.0000, nullable=False)
	__table_args__ = (
        db.PrimaryKeyConstraint('transaction_id', 'method_of_payment', name='payment_id'),
        db.CheckConstraint(
            "method_of_payment IN ('cash', 'debit', 'mastercard', 'visa', 'amex', 'insurance')", 
            name="check_method_of_payment"
        ),
    )

class insurance_payments(db.Model):
	__tablename__ ='insurance_payments'
	transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id', ondelete="CASCADE"),  default= 0)
	insurance_policy_id = db.Column(db.String(100), db.ForeignKey('insurance.policy_id', ondelete="CASCADE"), nullable=False)
	__table_args__ = (
        db.PrimaryKeyConstraint('transaction_id', 'insurance_policy_id'),
    )



