"""
1378. Replace Employee ID With The Unique Identifier
"""

SELECT unique_id, name 
FROM employees 
LEFT JOIN employeeuni ON employees.id = employeeuni.id