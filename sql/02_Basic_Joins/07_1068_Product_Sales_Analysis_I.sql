"""
1068. Product Sales Analysis I
"""

SELECT product_name, year, price 
FROM Sales 
JOIN Product ON Sales.product_id = Product.product_id