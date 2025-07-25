"""
1731. The Number of Employees Which Report to Each Employee
"""

SELECT manager.employee_id, manager.name, 
COUNT(DISTINCT employee.employee_id) AS reports_count, 
ROUND(AVG(employee.age)) AS average_age 
FROM Employees employee 
JOIN Employees manager 
ON employee.reports_to = manager.employee_id 
GROUP BY 1, 2 
ORDER BY manager.employee_id