"""

104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

"""

# Solution 1: Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(h)
# Best Case (balanced tree): O(log(n))
# Worst Case (degenerate tree): O(n)

# Where n is the number of nodes in the tree and h is the height of the tree.

class Solution: # type: ignore
    def maxDepth(self, root: TreeNode) -> int: # type: ignore
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


######## ######## ######## ######## ######## ######## ########


# Solution 2: Iterative DFS (Stack) [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution: # type: ignore
    def maxDepth(self, root: TreeNode) -> int: # type: ignore
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 3: Breadth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution: # type: ignore
    def maxDepth(self, root: TreeNode) -> int: # type: ignore
        if not root:
            return 0

        level = 0
        q = deque([root]) # type: ignore
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level