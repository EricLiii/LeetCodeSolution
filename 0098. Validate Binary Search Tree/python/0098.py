class Solution_1:
"""
Runtime: 52 ms, faster than 74.94% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 9.20% of Python3 online submissions for Validate Binary Search Tree.

二叉搜索树: 需要注意的是，左子树的所有节点都要比根节点小，而非只是其左孩子比其小，右子树同样。
这是很容易出错的一点是，很多人往往只考虑了每个根节点比其左孩子大比其右孩子小。
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