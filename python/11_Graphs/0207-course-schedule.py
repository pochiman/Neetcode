"""

207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where prerequisites[i] 
= [ai, bi] indicates that you must take course bi first if you want to take 
course ai.

• For example, the pair [0, 1], indicates that to take course 0 you have to 
  first take course 1.

Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 
you should also have finished course 1. So it is impossible.

"""

# Solution 1: Cycle Detection (DFS) [✔️]
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

# Where V is the number of courses and E is the number of prerequisites.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # type: ignore
        # map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        # 1 -> 2
        # 3 -> 4