"""
1045. Customers Who Bought All Products
"""

/*  For which customers does the amount of purchased 
    products match the amount of available products?  */

SELECT customer_id 
FROM Customer 
GROUP BY customer_id 
HAVING COUNT(DISTINCT product_key) = (

    -- amount of different products available
    SELECT COUNT(DISTINCT product_key) FROM Product
    )