class Solution:
"""
Runtime: 60 ms, faster than 70.39% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.5 MB, less than 51.43% of Python3 online submissions for Balanced Binary Tree.

Link: https://leetcode.com/problems/balanced-binary-tree/discuss/157645/Python-Tree-tm
"""
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True
        self.getHeight(root)
        return self.isBalanced
        
    
    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1: 
            self.isBalanced = False
        return max(left, right) + 1