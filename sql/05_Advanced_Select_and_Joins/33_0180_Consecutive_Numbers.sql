"""
180. Consecutive Numbers
"""

SELECT DISTINCT a.Num AS ConsecutiveNums 
FROM Logs a 
JOIN Logs b ON a.Id = b.Id + 1 AND a.Num = b.Num 
JOIN Logs c ON a.Id = c.Id + 2 AND a.Num = c.Num