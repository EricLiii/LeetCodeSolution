# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left,root.right)
    
    def is_mirror(self,left_node,right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        if left_node.val!=right_node.val:
            return False
        return self.is_mirror(right_node.right,left_node.left) and\
               self.is_mirror(left_node.right,right_node.left)
