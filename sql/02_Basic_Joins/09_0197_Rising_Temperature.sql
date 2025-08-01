"""
197. Rising Temperature
"""

-- Solution 1: [✔️]
SELECT w2.id 
FROM Weather w1 
JOIN Weather w2 
    ON DATEDIFF(w1.recordDate, w2.recordDate) = -1 
WHERE w2.temperature > w1.temperature

/*  There is another way of solve this problem, that is by using 
    window functions, wherein we could use the lag and lead 
    functions to get the previous day's information.  */ 

-- Solution 2: 
SELECT w2.id 
FROM Weather w1 
JOIN Weather w2 
    ON DATEDIFF(w1.recordDate, w2.recordDate) = -1 
    AND w2.temperature > w1.temperature


-- Solution 3: 
SELECT w2.id 
FROM Weather w1 
JOIN Weather w2 
    ON w1.recordDate - w2.recordDate = -1 
WHERE w2.temperature > w1.temperature