"""
1378. Replace Employee ID With The Unique Identifier
"""

SELECT unique_id, name 
FROM Employees 
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id