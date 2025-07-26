"""
596. Classes With at Least 5 Students
"""

-- Solution 1:
SELECT class 
FROM (
    SELECT class, COUNT(DISTINCT student) AS c 
    FROM courses 
    GROUP BY class
    ) AS temp
WHERE c >= 5


-- Solution 2:
SELECT class 
FROM courses 
GROUP BY class 
HAVING COUNT(DISTINCT student) >= 5

-- To filter out candidates.