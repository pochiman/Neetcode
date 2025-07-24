"""
1581. Customer Who Visited but Did Not Make Any Transactions
"""

-- Solution 1:
SELECT customer_id, COUNT(DISTINCT visit_id) AS count_no_trans 
FROM visits 
WHERE visit_id NOT IN (
    SELECT visit_id FROM transactions
    )
GROUP BY customer_id


-- Solution 2:
SELECT customer_id, 
COUNT(visits.visit_id) AS count_no_trans 
FROM visits 
LEFT JOIN transactions 
ON visits.visit_id = transactions.visit_id
WHERE transactions.visit_id IS NULL
GROUP BY customer_id