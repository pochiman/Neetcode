"""

1899. Merge Triplets to Form Target Triplet

A triplet is an array of three integers. You are given a 2D integer array triplets, 
where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an 
integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of 
times (possibly zero):

• Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become 
  [max(ai, aj), max(bi, bj), max(ci, cj)].

  • For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] 
    will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] as an element 
of triplets, or false otherwise.



Example 1:

Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last 
triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],
[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 
2 in any of the triplets.

Example 3:

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. 
Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. 
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. 
Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. 
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.

"""

# Solution 1: Greedy [✔️]
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution: # type: ignore
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool: # type: ignore
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3


######## ######## ######## ######## ######## ######## ########


# Solution 2: Greedy (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool: # type: ignore
        x = y = z = False
        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            if x and y and z:
                return True
        return False