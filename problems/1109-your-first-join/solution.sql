-- Employee name + department name
SELECT e.name, d.name AS department
FROM employees e
join departments as d on e.department_id = d.id