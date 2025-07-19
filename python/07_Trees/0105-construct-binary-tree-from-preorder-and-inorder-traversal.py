"""

105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same 
tree, construct and return the binary tree.



Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""

# Solution 1: Depth First Search [✔️]
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution: # type: ignore
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # type: ignore
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # type: ignore
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


######## ######## ######## ######## ######## ######## ########


# Solution 3: Depth First Search (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # type: ignore
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx]) # type: ignore
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))