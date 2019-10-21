class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 74.59% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.
"""
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.util(root)
        return root
    
    def util(self, root):
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)