"""
1633. Percentage of Users Attended a Contest
"""

SELECT 
    contest_id, 
    ROUND(COUNT(user_id) * 100 / (SELECT COUNT(user_id) FROM Users), 2) AS percentage 
FROM Register 
GROUP BY contest_id 
ORDER BY percentage DESC, contest_id ASC