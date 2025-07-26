"""
1327. List the Products Ordered in a Period
"""

SELECT product_name, SUM(unit) AS unit 
FROM Products 
JOIN Orders ON Products.product_id = Orders.product_id 
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02' 
GROUP BY product_name 
HAVING SUM(unit) >= 100