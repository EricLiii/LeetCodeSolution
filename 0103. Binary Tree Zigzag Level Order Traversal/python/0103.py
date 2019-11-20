# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
"""
Runtime: 40 ms, faster than 65.16% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result
        level_nodes=[root]
        toReverse=False
        while level_nodes:
            new_level_nodes=[]
            result.append([])
            for node in level_nodes:
                result[-1].append(node.val)
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            level_nodes=new_level_nodes
            if toReverse==True:
                result[-1]=result[-1][::-1]
                # Can't just result[-1][::-1], this only extract the result[-1] and do reversal 
            toReverse= not toReverse
        return result
        
class Solution:
"""
Author:Zefeng

Runtime: 36 ms, faster than 89.03% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        fromleft = True
        while stack:
            tmp = []
            tmp2 = []
            for node in stack: 
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                tmp2.append(node.val)
            if not fromleft:
                tmp2 = tmp2[::-1]
            fromleft = not fromleft
            stack = tmp
            res.append(tmp2)
        return res
