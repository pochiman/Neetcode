"""

1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on 
a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance 
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if 
there is exactly one simple path between any two points.



Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

"""

# Solution 2: Prim's Algorithm [✔️]
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)

class Solution: # type: ignore
    def minCostConnectPoints(self, points: List[List[int]]) -> int: # type: ignore
        N = len(points)
        adj = { i:[] for i in range(N) }  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH) # type: ignore
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei]) # type: ignore
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 3: Prim's Algorithm (Optimal)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: # type: ignore
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) + 
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res