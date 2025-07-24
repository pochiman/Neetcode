"""
1683. Invalid Tweets
"""

SELECT tweet_id 
FROM tweets 
WHERE LENGTH(content) > 15