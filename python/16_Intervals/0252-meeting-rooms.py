"""

252. Meeting Rooms

Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person 
could add all meetings to their schedule without any conflicts.



Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

Explanation:
• (0,30) and (5,10) will conflict
• (0,30) and (15,20) will conflict

Example 2:

Input: intervals = [(5,8),(9,15)]
Output: true

Note: 
• (0,8),(8,10) is not considered a conflict at 8

"""

# Solution 2: Sorting [✔️]
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on the sorting algorithm.

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: true if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True