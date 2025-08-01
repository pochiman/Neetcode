"""

199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side 
of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Example 3:

Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []

"""

# Solution 2: Breadth First Search [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]: # type: ignore
        res = []
        q = collections.deque([root]) # type: ignore

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)
        return res