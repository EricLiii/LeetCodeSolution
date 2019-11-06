class Solution_1:
"""
Runtime: 52 ms, faster than 74.94% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 9.20% of Python3 online submissions for Validate Binary Search Tree.
"""
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, node, low, high):
        if not node:
            return True
        if node.val >= high or node.val <= low:
            return False
        left = self.helper(node.left, low, node.val)
        right = self.helper(node.right, node.val, high)
        return left and right