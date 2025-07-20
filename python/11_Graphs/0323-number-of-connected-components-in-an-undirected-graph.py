"""

323. Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes. There is also an edges array, where 
edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1

Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2

"""

# Solution 3: Disjoint Set Union (Rank | Size) [✔️]
# Time Complexity: O(V + (E * α(V)))
# Space Complexity: O(V)

# Where V is the number of vertices and E is the number of edges in the graph.
# α() is used for amortized complexity.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: # type: ignore
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res