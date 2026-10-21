-- Employees per department
SELECT department_id, COUNT(*) AS headcount
FROM Employees
group by department_id
