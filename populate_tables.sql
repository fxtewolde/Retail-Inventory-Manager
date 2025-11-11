INSERT INTO locations (id, street_address, suite_no, city, province, postal_code, pharmacy_owner)
VALUES 
(1, '22 Apple st', 222, 'Toronto', 'Ontario', '111222', 'A'),
(2, '123 Orange Ave', 101, 'Toronto', 'Ontario', '222333', 'B'),
(3, '456 Banana Blvd', 303, 'Toronto', 'Ontario', '333444', 'C'),
(4, '789 Cherry Dr', 404, 'Toronto', 'Ontario', '444555', 'D'),
(5, '101 Grape Ln', 505, 'Toronto', 'Ontario', '555666', 'E');
INSERT INTO departments (id, department_name)
VALUES (1, 'Retail');
INSERT INTO departments
VALUES (2, 'Pharmacy');
INSERT INTO departments
VALUES (3, 'Pharmacy');
INSERT INTO departments
VALUES (4, 'Health');
INSERT INTO departments
VALUES (5, 'Cosmetics');


INSERT INTO employees (id, first_name, last_name, telephone, employee_password, department_id, location_id, supervisor_id, payroll_id)
VALUES (1, 'Alice', 'Smith', '1-555-123-4567', '4958323', 1, 1, 0, 1);
INSERT INTO employees 
VALUES (2, 'Bob', 'Johnson', '555-987-6543', '232284848', 2, 2, 0, 2);
INSERT INTO employees 
VALUES (3, 'Charlie', 'Williams', '555-321-0987', '38473666', 1, 3, 0, 3);
INSERT INTO employees
VALUES (4, 'Diana', 'Brown', '555-654-3210', '484848593', 3, 4, 0, 4);
INSERT INTO employees 
VALUES (5, 'Edward', 'Jones', '555-456-7890', '57393993933', 4, 5, 0, 5);


INSERT INTO customers (id, first_name, last_name, telephone, email)
VALUES (1, 'Jessica', 'Taylor', '1-555-111-2222','jessica@example.com');
INSERT INTO customers
VALUES (2, 'Michael', 'Lee', '1-555-222-3333','michael@example.com');
INSERT INTO customers
VALUES (3, 'Sarah', 'Kim', '1-555-333-4444', 'sarah@example.com');
INSERT INTO customers
VALUES (4, 'David', 'Chen', '1-555-444-5555','david@example.com');
INSERT INTO customers
VALUES (5, 'Emma', 'Garcia', '1-555-555-6666', 'emma@example.com');


INSERT INTO optimum_members (id, optimum_points, customer_id)
VALUES (1, 1000, 1);
INSERT INTO optimum_members
VALUES (2, 2432, 2);
INSERT INTO optimum_members
VALUES (3, 0, 3);
INSERT INTO optimum_members
VALUES (4, 900002, 4);
INSERT INTO optimum_members
VALUES (5, 39654, 5);


INSERT INTO suppliers (id, supplier_name, telephone, email, credit_owing, total_owing)
VALUES (1, 'Supplier One', '1-555-777-8888', 'supplier1@example.com', 500.00, 1000.00);
INSERT INTO suppliers
VALUES (2, 'Supplier Two', '1-555-888-9999','supplier2@example.com', 300.0000, 750.0000);
INSERT INTO suppliers
VALUES (3, 'Supplier Three', '1-555-999-0000','supplier3@example.com', 100.0000, 200.0000);
INSERT INTO suppliers
VALUES (4, 'Supplier Four', '1-555-000-1111','supplier4@example.com', 250.0000, 500.0000);
INSERT INTO suppliers
VALUES (5, 'Supplier Five', '1-555-111-2222', 'supplier5@example.com', 400.0000, 900.0000);



INSERT INTO product_details (upc_a, product_name, category, details)
VALUES ('0-12345-67890-1', 'Aspirin', 'Medications', 'Pain reliever.');
INSERT INTO product_details
VALUES ('0-23456-78901-2', 'Vitamins', 'Health', 'Daily vitamins.');
INSERT INTO product_details
VALUES ('0-34567-89012-3', 'Shampoo', 'Cosmetics', 'Hair care product.');
INSERT INTO product_details
VALUES ('0-45678-90123-4', 'Bread', 'Grocery', 'Whole grain bread.');
INSERT INTO product_details
VALUES ('0-56789-01234-5', 'Moisturizer', 'Cosmetics', 'Hydrating lotion.');



INSERT INTO products (id, upc_a, department_id, supplier_id, retail_price, unit_price)
VALUES (1, '0-12345-67890-1', 1, 1, 9.99, 5.99);
INSERT INTO products
VALUES (2, '0-23456-78901-2', 2, 2, 19.99, 10.00);
INSERT INTO products
VALUES (3, '0-34567-89012-3', 3, 3, 12.99, 6.75);
INSERT INTO products
VALUES (4, '0-45678-90123-4', 4, 4, 3.49, 1.59);
INSERT INTO products
VALUES (5, '0-56789-01234-5', 5, 5, 500, 100);


INSERT INTO medications
VALUES ('87654321', 2);
INSERT INTO medications
VALUES ('23456789', 3);
INSERT INTO medications
VALUES ('98765432', 4);
INSERT INTO medications
VALUES ('34567890', 5);


INSERT INTO patients (customer_id, spouse_id, parent_1_id, parent_2_id)
VALUES (1, 2, 3, 4);
INSERT INTO patients
VALUES (2, 1, 4, 5);
INSERT INTO patients
VALUES (3, 5, 1, 2);
INSERT INTO patients
VALUES (4, 3, 2, 1);
INSERT INTO patients
VALUES (5, 4, 1, 3);


INSERT INTO prescriptions (id, customer_id, drug_indentification_number, practitioner_mnic)
VALUES (1, 1, '00000000', 'DOC-1234');
INSERT INTO prescriptions
VALUES (2, 2, '12345678', 'DOC-2345');
INSERT INTO prescriptions
VALUES (3, 3, '87654321', 'DOC-3456');
INSERT INTO prescriptions
VALUES (4, 4, '11112222', 'DOC-4567');
INSERT INTO prescriptions
VALUES (5, 5, '22223333', 'DOC-5678');


INSERT INTO transactions (id, employee_id, location_id, customer_id, subtotal, transaction_date)
VALUES (1, 1, 1, 1, 20.00, '2024-04-30 12:13:34');
INSERT INTO transactions
VALUES (2, 2, 2, 2, 15.00, '2021-09-30 12:13:34');
INSERT INTO transactions
VALUES (3, 3, 3, 3, 30.00, '2024-09-30 17:13:34');
INSERT INTO transactions
VALUES (4, 4, 4, 4, 25.00, '2012-09-30 17:13:34');
INSERT INTO transactions
VALUES (5, 5, 5, 5, 40.00, '2024-11-30 17:13:34');


INSERT INTO orders (id, placed_on, expected_on, received_on)
VALUES (1, '2024-09-30 22:13:34', '2024-10-07 22:13:34', '2024-10-01 22:13:34');
INSERT INTO orders
VALUES (2, '2010-09-30 22:13:34', '2010-10-07 22:13:34', '2012-10-20 22:13:34');
INSERT INTO orders
VALUES (3, '2024-09-30 22:13:34', '2024-11-07 22:13:34', '2024-12-03 22:13:34');
INSERT INTO orders
VALUES (4, '2024-05-23 22:13:34', '2024-07-23 22:13:34', '2024-08-12 22:13:34');
INSERT INTO orders
VALUES (5, '2017-02-25 22:13:34', '2017-05-07 22:13:34', '2017-05-09 22:13:34');



INSERT INTO order_details (order_id, product_id,  quantity)
VALUES (1, 1, 10);
INSERT INTO order_details
VALUES (2, 2, 80);
INSERT INTO order_details
VALUES (3, 3, 5);
INSERT INTO order_details
VALUES (4, 4, 3);
INSERT INTO order_details
VALUES (5, 5, 120);

INSERT INTO insurance (policy_id, customer_id, company_name)
VALUES ('POL12345', 1, 'Insurance Co A');
INSERT INTO insurance
VALUES ('POL23456', 2, 'Insurance Co B');
INSERT INTO insurance
VALUES ('POL34567', 3, 'Insurance Co C');
INSERT INTO insurance
VALUES ('POL45678', 4, 'Insurance Co D');
INSERT INTO insurance
VALUES ('POL56789', 5, 'Insurance Co E');



INSERT INTO filled_prescriptions (precription_id, fill_date)
VALUES (1, CURRENT_TIMESTAMP);
INSERT INTO filled_prescriptions
VALUES (2, CURRENT_TIMESTAMP);
INSERT INTO filled_prescriptions
VALUES (3, CURRENT_TIMESTAMP);
INSERT INTO filled_prescriptions
VALUES (4, CURRENT_TIMESTAMP);
INSERT INTO filled_prescriptions
VALUES (5, CURRENT_TIMESTAMP);



INSERT INTO inventory (product_id, location_id, quantity, on_backorder)
VALUES (1, 1, 100, 0);
INSERT INTO inventory
VALUES (2, 2, 50, 1);
INSERT INTO inventory
VALUES (3, 3, 200, 0);
INSERT INTO inventory
VALUES (4, 4, 0, 1);
INSERT INTO inventory
VALUES (5, 5, 150, 0);



INSERT INTO product_sales (transaction_id, product_id, discount, tax_rate, quantity)
VALUES (1, 1, 0.50, 0.13, 2);
INSERT INTO product_sales
VALUES (2, 2, 1.00, 0.13, 1);
INSERT INTO product_sales
VALUES (3, 3, 0.00, 0.13, 5);
INSERT INTO product_sales
VALUES (4, 4, 0.25, 0.13, 3);
INSERT INTO product_sales
VALUES (5, 5, 0.75, 0.13, 4);



INSERT INTO payments (transaction_id, method_of_payment, total_paid)
VALUES (1, 'cash', 20.00);
INSERT INTO payments 
VALUES (2, 'mastercard', 15.00);
INSERT INTO payments
VALUES (3, 'debit', 30.00);
INSERT INTO payments
VALUES (4, 'insurance', 25.00);
INSERT INTO payments
VALUES (5, 'cash', 40.00);



INSERT INTO insurance_payments(transaction_id, insurance_policy_id)
VALUES (1, 'HEALTH12098769');
INSERT INTO insurance_payments
VALUES (1, 'HEALTH12376893');
INSERT INTO insurance_payments
VALUES (1, 'HOME123456y3');
INSERT INTO insurance_payments
VALUES (1, 'HEALTH98765431');
INSERT INTO insurance_payments
VALUES (1, 'HOME123456789');