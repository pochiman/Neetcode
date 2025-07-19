"""

110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

"""

# Solution 2: Depth First Search [✔️]
# Time Complexity: O(n)
# Space Complexity: O(h)
# Best Case (balanced tree): O(log(n))
# Worst Case (degenerate tree): O(n)

# Where n is the number of nodes in the tree and h is the height of the tree.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: # type: ignore

        def dfs(root):
            if not root: 
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]