"""
1789. Primary Department for Each Employee
"""

-- primary_flag set to 'Y'
SELECT employee_id, department_id 
FROM Employee 
WHERE primary_flag = 'Y' 

UNION 

-- employees that only have one department
SELECT employee_id, department_id 
FROM Employee 
GROUP BY 1 
HAVING COUNT(*) = 1