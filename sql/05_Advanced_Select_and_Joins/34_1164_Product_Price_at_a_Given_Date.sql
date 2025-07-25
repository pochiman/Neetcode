"""
1164. Product Price at a Given Date
"""

SELECT DISTINCT Products.product_id, IFNULL(latest_prices.new_price, 10) AS price
FROM Products
LEFT JOIN (
    SELECT product_id, new_price FROM Products 
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date) AS change_date 
        FROM Products 
        WHERE change_date <= '2019-08-16' 
        GROUP BY product_id
        )) latest_prices 
ON Products.product_id = latest_prices.product_id