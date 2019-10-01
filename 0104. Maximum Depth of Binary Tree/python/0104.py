# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def maxDepth(self, root: TreeNode) -> int:
        len=0;
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right: 
            len=self.maxDepth(root.left)+1
        if not root.left and root.right:
            len=self.maxDepth(root.right)+1
        if root.left and root.right:
            len=max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        return len
        
class Solution_2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # not None equals to True
 
class Solution:
"""
Author: Zefeng

Runtime: 44 ms, faster than 93.29% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16 MB, less than 12.50% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [1]
        self.helper(root, 1, res)
        return max(res)
        
    def helper(self, node, depth, res):
        if not node:
            return 
        if not node.left and not node.right:
            res.append(depth)
            return
        self.helper(node.left, depth+1, res)
        self.helper(node.right, depth+1, res)
        return