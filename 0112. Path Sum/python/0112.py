class Solution:
"""
Runtime: 52 ms, faster than 62.16% of Python3 online submissions for Path Sum.
Memory Usage: 15.9 MB, less than 5.45% of Python3 online submissions for Path Sum.
"""
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)