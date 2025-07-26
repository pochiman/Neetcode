"""
1517. Find Users With Valid E-Mails
"""

-- original solution: [✖️]
SELECT * 
FROM Users 
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'


-- working solution: [✔️]
SELECT user_id, name, mail 
FROM Users 
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$' 
AND mail LIKE BINARY '%@leetcode.com'