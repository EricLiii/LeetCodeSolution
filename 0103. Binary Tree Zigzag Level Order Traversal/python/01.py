# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
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
