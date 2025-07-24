"""
1581. Customer Who Visited but Did Not Make Any Transactions
"""

-- Solution 1: [✔️]
SELECT customer_id, COUNT(DISTINCT visit_id) AS count_no_trans 
FROM Visits 
WHERE visit_id NOT IN (
    SELECT visit_id FROM Transactions
    )
GROUP BY customer_id


-- Solution 2: 
SELECT customer_id, 
COUNT(DISTINCT Visits.visit_id) AS count_no_trans 
FROM Visits 
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id 
WHERE Transactions.transaction_id IS NULL 
GROUP BY customer_id