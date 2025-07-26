"""
619. Biggest Single Number
"""

-- Solution 1:
SELECT MAX(num) AS num 
FROM (
    SELECT num 
    FROM MyNumbers 
    GROUP BY num
    HAVING COUNT(*) = 1
    ) single_numbers


-- Solution 2:
SELECT num 
FROM MyNumbers 
GROUP BY num 
HAVING COUNT(num) = 1 

UNION 

SELECT NULL AS num 
ORDER BY num DESC 
LIMIT 1