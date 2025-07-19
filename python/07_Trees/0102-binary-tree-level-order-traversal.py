"""

102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

"""

# Solution 2: Breadth First Search [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]: # type: ignore
        res = []

        q = collections.deque() # type: ignore
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res