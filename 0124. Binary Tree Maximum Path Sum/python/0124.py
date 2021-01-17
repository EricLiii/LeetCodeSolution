class Solution:
"""
Runtime: 92 ms, faster than 41.37% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 20.9 MB, less than 88.83% of Python3 online submissions for Binary Tree Maximum Path Sum.

https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
"""
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if not root:
            return 0
        
        gain_on_left = max(self.dfs(root.left), 0)
        gain_on_right = max(self.dfs(root.right), 0)
        self.res = max(self.res, gain_on_left + root.val + gain_on_right)
        
        return root.val + max(gain_on_left, gain_on_right)