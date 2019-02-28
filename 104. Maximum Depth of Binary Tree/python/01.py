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
 
