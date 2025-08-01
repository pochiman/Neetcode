"""
1204. Last Person to Fit in the Bus
"""

SELECT a.person_name 
FROM Queue a 
JOIN Queue b 
ON a.turn >= b.turn 
GROUP BY a.turn 
HAVING SUM(b.weight) <= 1000 
ORDER BY a.turn DESC 
LIMIT 1