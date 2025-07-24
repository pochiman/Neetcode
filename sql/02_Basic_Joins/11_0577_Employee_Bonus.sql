"""
577. Employee Bonus
"""

-- Solution 1: [✔️]
SELECT name, bonus 
FROM Employee 
LEFT JOIN Bonus ON Employee.empId = Bonus.empId 
WHERE bonus < 1000 OR bonus IS NULL


-- Solution 2: 
SELECT name, bonus 
FROM Employee 
LEFT JOIN Bonus ON Employee.empId = Bonus.empId 
WHERE COALESCE(bonus, 0) < 1000