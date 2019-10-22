class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 64.76% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
"""
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.helper(root, [])
        for i in range(len(self.res)):
            self.res[i] = "->".join(self.res[i])
        return self.res
        
    def helper(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            self.res.append(path +[str(node.val)])

        self.helper(node.left, path + [str(node.val)])
        self.helper(node.right, path + [str(node.val)])
        return
        
class Solution_2:
"""
Runtime: 40 ms, faster than 64.76% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.6 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.

递归.
避免了在列表中插入"->". 这个要记.
"""
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.res = []
        self.helper(root, "")
        return self.res
        
    def helper(self, node, path):
        if not node.left and not node.right:
            self.res.append(path + str(node.val))
            return
        if node.left:
            self.helper(node.left, path + str(node.val) + "->")
        if node.right:
            self.helper(node.right, path + str(node.val) + "->")
            
class Solution_3:
"""
Runtime: 36 ms, faster than 88.04% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.

迭代.
这个也要记.
"""
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res