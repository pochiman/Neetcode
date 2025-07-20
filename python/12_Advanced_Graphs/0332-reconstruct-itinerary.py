"""

332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent 
the departure and the arrival airports of one flight. Reconstruct the itinerary 
in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary 
must begin with "JFK". If there are multiple valid itineraries, you should return 
the itinerary that has the smallest lexical order when read as a single string.

• For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than 
  ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all 
the tickets once and only once.



Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],
["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK",
"ATL","SFO"] but it is larger in lexical order.

"""

# Solution 1: Depth First Search [✔️]
# Time Complexity: O(E * V)
# Space Complexity: O(E * V)

# Where E is the number of tickets (edges) and V is the number of airports (vertices).

class Solution: # type: ignore
    def findItinerary(self, tickets: List[List[str]]) -> List[str]: # type: ignore
        adj = { src : [] for src, dst in tickets }

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res


######## ######## ######## ######## ######## ######## ######## ########


# Refactor solution to pass updated test cases.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]: # type: ignore
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(adj, result, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src][:]
            res.append(src)

        dfs(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res