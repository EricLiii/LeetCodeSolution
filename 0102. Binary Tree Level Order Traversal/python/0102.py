# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result
        level_nodes=[root]
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
        return result

class Solution_2:
"""
Runtime: 40 ms, faster than 80.33% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.8 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.

Link: https://www.cnblogs.com/bjwu/p/9284534.html
"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return
            else:
                sol[level-1].append(node.val)
                if len(sol) == level:
                    sol.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        sol = [[]]
        helper(root, 1)
        return sol[:-1]