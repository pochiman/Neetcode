"""
1683. Invalid Tweets
"""

-- Solution 1:
SELECT tweet_id 
FROM Tweets 
WHERE LENGTH(content) > 15


-- Solution 2:
SELECT tweet_id 
FROM Tweets 
WHERE CHAR_LENGTH(content) > 15