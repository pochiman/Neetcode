"""

84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the 
width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

"""

# Solution 4: Stack (One Pass) [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution: # type: ignore
    def largestRectangleArea(self, heights: List[int]) -> int: # type: ignore
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


######## ######## ######## ######## ######## ######## ########


# Solution 5: Stack (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: # type: ignore
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea