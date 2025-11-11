SELECT * FROM locations; 


SELECT MIN(optimum_points) AS minimum, MAX(optimum_points) AS maximum, AVG(optimum_points) AS average
FROM optimum_members;

SELECT COUNT(*) AS cash_payments_made
FROM payments
WHERE method_of_payment = 'cash';


SELECT first_name ||' '|| last_name as name, telephone
FROM employees
UNION
SELECT first_name ||' '|| last_name as name, telephone
FROM customers
UNION
SELECT supplier_name as name, telephone
FROM suppliers
ORDER BY name DESC; 


SELECT department_id, COUNT(*) AS num_employees
FROM employees
GROUP BY department_id;
