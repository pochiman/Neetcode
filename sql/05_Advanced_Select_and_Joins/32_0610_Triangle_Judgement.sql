"""
610. Triangle Judgement
"""

SELECT x, y, z, 
IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle 
FROM Triangle