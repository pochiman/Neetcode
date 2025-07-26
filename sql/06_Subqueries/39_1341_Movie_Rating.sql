"""
1341. Movie Rating
"""

/*  Find the name of the user who has rated the greatest number of movies. 
    In case of a tie, return the lexicographically smaller user name.   */

SELECT name AS results 
FROM (
    SELECT user_id, name, COUNT(*) 
    FROM Users 
    JOIN MovieRating 
    USING (user_id) 
    GROUP BY 1, 2 
    ORDER BY 3 DESC, 2 ASC 
    LIMIT 1
    ) users 

UNION ALL 

/*  Find the movie name with the highest average rating in February 2020. 
    In case of a tie, return the lexicographically smaller movie name.  */

SELECT title AS results 
FROM (
    SELECT movie_id, title, AVG(rating) 
    FROM Movies 
    JOIN MovieRating 
    USING (movie_id) 
    WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02' 
    GROUP BY 1, 2 
    ORDER BY 3 DESC, 2 ASC
    LIMIT 1
    ) movies