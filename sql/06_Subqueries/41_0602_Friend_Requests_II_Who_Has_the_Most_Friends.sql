"""
602. Friend Requests II: Who Has the Most Friends
"""

-- Solution 1:
SELECT id, COUNT(*) AS num 
FROM (
    SELECT requester_id AS id 
    FROM RequestAccepted 
    UNION ALL 
    SELECT accepter_id AS id 
    FROM RequestAccepted
    ) ids 
GROUP BY id 
ORDER BY num DESC 
LIMIT 1


-- Solution 2:
SELECT id, SUM(n) AS num 
FROM (
    SELECT accepter_id AS id, COUNT(1) AS n 
    FROM RequestAccepted 
    GROUP BY accepter_id 
    UNION ALL 
    SELECT requester_id AS id, COUNT(1) AS n 
    FROM RequestAccepted 
    GROUP BY requester_id
    ) lookup 
GROUP BY id 
ORDER BY num DESC 
LIMIT 1