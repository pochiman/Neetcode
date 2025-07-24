""" 
1757. Recyclable and Low Fat Products 
"""

-- Solution 1: [✔️]
SELECT name 
FROM Customer 
WHERE referee_id IS NULL OR referee_id != 2

/*  the referee_id IS NULL OR referee_id != 2 solution 
    might be the best solution here as the referee_id 
    could theoretically be 0    */

-- Solution 2:
SELECT name 
FROM Customer
WHERE COALESCE(referee_id, 0) != 2


-- Solution 3:
SELECT name 
FROM Customer
WHERE IFNULL(referee_id, 0) != 2