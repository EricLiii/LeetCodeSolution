class Solution_1:
"""
Runtime: 32 ms, faster than 93.29% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for Binary Tree Preorder Traversal.

递归.
"""
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
        return
        
class Solution_2:
"""
Runtime: 32 ms, faster than 93.29% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.8 MB, less than 6.52% of Python3 online submissions for Binary Tree Preorder Traversal.

迭代.
"""
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret