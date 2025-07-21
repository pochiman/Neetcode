"""

253. Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number 
of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.



Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2

Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]
Output: 1

"""

# Solution 3: Two Pointers [✔️]
# Time Complexity: O(n log n)
# Space Complexity: O(n)

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
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res