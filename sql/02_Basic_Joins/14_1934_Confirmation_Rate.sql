"""
1934. Confirmation Rate
"""

SELECT Signups.user_id, COALESCE(ROUND(AVG(action = 'confirmed'), 2), 0) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations 
USING (user_id)
GROUP BY Signups.user_id