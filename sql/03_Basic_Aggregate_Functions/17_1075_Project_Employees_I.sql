"""
1075. Project Employees I
"""

SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years 
FROM Project 
JOIN Employee 
    ON Project.employee_id = Employee.employee_id 
GROUP BY project_id