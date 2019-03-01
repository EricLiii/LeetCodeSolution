# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder.pop()) #pop()是倒序弹出
        posi=inorder.index(root.val)
        root.right=self.buildTree(inorder[posi+1:],postorder) # 因为postorder是左->右->根，所以倒序弹出的话剩下的是右，所以先root.right
        root.left=self.buildTree(inorder[0:posi],postorder) 
        
        return root
