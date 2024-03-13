#Task 2
"""
Select queries

Use the sample SQLite database hr.db

As a solution to HW, create a file named: task2.sql with all SQL queries:

write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
write a query to get the unique department ID from the employee table
write a query to get all employee details from the employee table ordered by first name, descending
write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
write a query to get the maximum and minimum salary from the employees table
write a query to get a monthly salary (round 2 decimal places) of each and every employee
"""

import sqlite3

conn = sqlite3.connect("data_base.db")
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")
print()
 
cursor = conn.cursor()



cursor.execute("SELECT * FROM employees;")
data = cursor.fetchmany(10)
for row in data:
    print(row)

cursor.execute("SELECT first_name AS 'First Name', last_name AS 'Last Name' FROM employees;")
cursor.execute("SELECT DISTINCT department_id FROM employees;")
cursor.execute("SELECT * FROM employees ORDER BY first_name DESC;")
cursor.execute("SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;")
cursor.execute("SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;")
cursor.execute("SELECT first_name, last_name, ROUND(salary/12, 2) AS monthly_salary FROM employees;")

conn.close()
