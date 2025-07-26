"""
585. Investments in 2016
"""

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance 
WHERE tiv_2015 IN (

    -- have the same tiv_2015 value as one or more other policyholders, and
    SELECT tiv_2015 
    FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
    ) 

AND (lat, lon) IN (

    -- are not located in the same city as any other policyholder  
    -- (i.e., the (lat, lon) attribute pairs must be unique)
    SELECT lat, lon 
    FROM Insurance 
    GROUP BY lat, lon 
    HAVING COUNT(*) = 1
    )