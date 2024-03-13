--Task 1
-- 1. write a query in SQL to display the first name,
-- last name, department number, and department name for each employee
SELECT employees.first_name,
       employees.last_name,
       employees.department_id,
       departments.depart_name
FROM   employees,
       departments
       JOIN main.department d
         ON employees.department_id = d.department_id;
-- -----------------------------------------------------------

-- 2. write a query in SQL to display the first and last name,
-- department, city, and state province for each employee
SELECT employees.first_name,
       employees.last_name,
       departments.depart_name,
       locations.city,
       locations.state_province
FROM   employees
       INNER JOIN departments
               ON employees.department_id = departments.department_id
       INNER JOIN locations
               ON departments.location_id = locations.location_id;
-- -----------------------------------------------------------

-- 3. write a query in SQL to display the first name, last name,
-- department number, and department name, for all employees for
-- departments 80 or 40
SELECT employees.first_name,
       employees.last_name,
       departments.department_id,
       departments.depart_name
FROM   employees
       INNER JOIN departments
               ON employees.department_id = departments.department_id
WHERE  employees.department_id LIKE 80
        OR employees.department_id LIKE 40;
-- -----------------------------------------------------------

-- 4. write a query in SQL to display all departments including those
-- where does not have any employee
SELECT departments.depart_name,
       employees.first_name,
       employees.last_name
FROM   departments
       LEFT JOIN employees
              ON employees.department_id = departments.department_id
-- -----------------------------------------------------------

-- 5. write a query in SQL to display the first name of all employees
-- including the first name of their manager
SELECT employees.first_name AS "emploee_mane",
       e.first_name         AS "manager_name"
FROM   employees
       JOIN employees AS e
         ON employees.manager_id = e.employee_id;
-- -----------------------------------------------------------

-- 6. write a query in SQL to display the job title, full name (first and last name )
-- of the employee, and the difference between the maximum salary for the job
-- and the salary of the employee
SELECT jobs.job_title,
       employees.first_name || ' ' || employees.last_name AS "full name",
       jobs.max_salary - employees.salary AS "difference"
FROM   employees
       JOIN jobs
         ON employees.job_id = jobs.job_id;
-- -----------------------------------------------------------

-- 7. write a query in SQL to display the job title and the average salary of employees
SELECT jobs.job_title,
       Avg(employees.salary) AS "average salary"
FROM   jobs,
       employees
WHERE  employees.job_id = jobs.job_id
GROUP  BY jobs.job_id;
-- -----------------------------------------------------------

-- 8. write a query in SQL to display the full name (first and last name),
-- and salary of those employees who work in any department located in London
SELECT employees.first_name || ' ' || employees.last_name AS "full name",
       employees.salary
FROM   employees,
       departments,
       locations
WHERE  employees.department_id = departments.department_id
       AND departments.location_id = locations.location_id
       AND locations.city LIKE 'London';
-- -----------------------------------------------------------

-- 9. write a query in SQL to display the department name and the number
-- of employees in each department
SELECT departments.depart_name,
       Count(employee_id)
FROM   departments,
       employees
WHERE  employees.department_id = departments.department_id
GROUP  BY departments.depart_name;
-- -----------------------------------------------------------