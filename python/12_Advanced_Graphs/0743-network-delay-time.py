"""

743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the 
source node, vi is the target node, and wi is the time it takes for a signal to 
travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for 
all the n nodes to receive the signal. If it is impossible for all the n nodes 
to receive the signal, return -1.



Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

"""

# Solution 5: Dijkstra's Algorithm [✔️]
# Time Complexity: O(E log V)
# Space Complexity: O(V + E)

# Where V is the number of vertices and E is the number of edges.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: # type: ignore
        edges = collections.defaultdict(list) # type: ignore
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap) # type: ignore
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2)) # type: ignore

        return t if len(visit) == n else -1

        # O(E * logV)