"""

56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

# Solution 1: Sorting [✔️]
# Time Complexity: O(n log n)
# Space Complexity: 
#   - O(1) or O(n) space depending on the sorting algorithm.
#   - O(n) for the output list.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # type: ignore
        # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output