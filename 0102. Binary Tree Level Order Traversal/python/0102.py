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
                if len(sol) == level: #当len(sol) > level的时候，说明已经添加了[]了，无需重复添加.
                    sol.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        sol = [[]]
        helper(root, 1)
        return sol[:-1]
        
class Solution_3:
"""
Author: Zefeng

Runtime: 40 ms, faster than 80.87% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.9 MB, less than 20.97% of Python3 online submissions for Binary Tree Level Order Traversal.

迭代.
"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:   
            return []
        stack = [root]
        res = []
        while stack:
            tmp = []
            tmp2 = []
            for node in stack:  
                if node.left:             
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                tmp2.append(node.val)
            stack = tmp
            res.append(tmp2)
        return res

class Solution_4:
"""
Author: Zefeng
Runtime: 40 ms, faster than 81.73% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.5 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.

递归.
"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[]]
        self.utils(root, 0, res)
        return res
    
    def utils(self, node, depth, res):
        if not node:
            return
        if len(res) < depth+1:
            res.append([])
        res[depth].append(node.val)
        if node.left:
            self.utils(node.left, depth+1, res)
        if node.right:
            self.utils(node.right, depth+1, res)