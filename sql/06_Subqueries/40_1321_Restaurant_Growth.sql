"""
1321. Restaurant Growth
"""

-- Solution 1: self join
SELECT 
    a.visited_on, 
    SUM(amount) AS amount, 
    ROUND((SUM(amount) / 7), 2) AS average_amount 
FROM (
    SELECT DISTINCT visited_on 
    FROM Customer
    ) a
JOIN Customer b 
ON DATEDIFF(a.visited_on, b.visited_on) 
BETWEEN 0 AND 6 
GROUP BY a.visited_on 
HAVING COUNT(DISTINCT b.visited_on) = 7 
ORDER BY a.visited_on


-- Solution 2: window functions
SELECT DISTINCT visited_on, 
    SUM(amount) OVER (
        ORDER BY visited_on ASC 
        RANGE BETWEEN INTERVAL 6 DAY 
        PRECEDING AND CURRENT ROW
        ) AS amount, 
    ROUND((SUM(amount) OVER (
        ORDER BY visited_on ASC 
        RANGE BETWEEN INTERVAL 6 DAY 
        PRECEDING AND CURRENT ROW
        ) / 7), 2) AS average_amount 

FROM Customer 

LIMIT 100000000000 OFFSET 6