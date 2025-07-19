"""

100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they 
are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.



Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

"""

# Solution 1: Depth First Search [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)
# Best Case (balanced tree): O(log(n))
# Worst Case (degenerate tree): O(n)

# Where n is the number of nodes in the tree and h is the height of the tree.

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: # type: ignore
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))