"""
1667. Fix Names in a Table
"""

-- Solution 1:
SELECT user_id, 
CONCAT(UPPER(LEFT(name, 1)), 
LOWER(RIGHT(name, LENGTH(name) - 1))) AS name 
FROM Users 
ORDER BY user_id


-- Solution 2:
SELECT user_id, 
CONCAT(UPPER(LEFT(name, 1)), 
LOWER(SUBSTRING(name, 2))) AS name 
FROM Users 
ORDER BY user_id