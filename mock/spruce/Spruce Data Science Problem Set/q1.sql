-- Please put your answer to Question 1 here!
-- Select department_id
SELECT e.department_id
-- alias avg to average_salary
, avg(amount) as average_salary
FROM employees e
-- Join to salaries (alias s)
JOIN salaries s ON s.emp_id = e.emp_id
GROUP BY e.department_id
-- Order results in ascending order 
ORDER BY e.department_id ASC;
