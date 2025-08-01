r"""

226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.



Example 1:

Input: root = [4,2,7,1,3,6,9]

     4 
   /   \
  2     7
 / \   / \
1   3 6   9  

Output: [4,7,2,9,6,3,1]

     4 
   /   \ 
  7     2
 / \   / \
9   6 3   1

Example 2:

Input: root = [2,1,3]

  2
 / \
1   3

Output: [2,3,1]

  2
 / \
3   1

Example 3:

Input: root = []
Output: []

"""

# Solution 2: Depth First Search [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack.

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: # type: ignore
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root