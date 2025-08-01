"""

739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return 
an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature. If there is no future day for which this 
is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

"""

# Solution 2: Stack [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # type: ignore
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res