"""
550. Game Play Analysis IV
"""

SELECT ROUND(COUNT(DISTINCT b.player_id) / COUNT(DISTINCT a.player_id), 2) AS fraction 
FROM (
    SELECT player_id, MIN(event_date) AS event_date 
    FROM Activity 
    GROUP BY player_id
    ) a 
    LEFT JOIN Activity b ON a.player_id = b.player_id AND DATEDIFF(b.event_date, a.event_date) = 1

/*  The only difference here is changing the left join date condition from 
    a.event_date+1 = b.event_date to DATEDIFF(b.event_date, a.event_date) = 1. 
    You could also use DATE_ADD(a.event_date, INTERVAL 1 DAY) = b.event_date.

    This is necessary as the new test case has Feb 29th as input which only occurs in 
    a leap year. These special dates are only handled correctly by date manipulation 
    functions such as DATE_ADD and DATEDIFF. What's to learn from this is that it's 
    always best practice to use date manipulation functions instead of being lazy and 
    using normal operations such a +1 and -1.   */