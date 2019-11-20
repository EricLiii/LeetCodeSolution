# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
"""
Author: Zefeng

Runtime: 128 ms, faster than 60.21% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 52.8 MB, less than 39.20% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

Idea:
跟第105题唯一不同之处就是需要先填补右子树，然后再填补左子树。
第105题中有一个解法时先reverse()再处理。这里就没有必要了，因为postorder的最后一个元素是根，所以直接pop()就行。
"""
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder[-1])
            ind = inorder.index(postorder.pop())
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
            
class Solution_2:
"""
有空想一下这道题的iterative solution.
"""
            
