class Solution_1:
"""
Author: Zefeng

Runtime: 44 ms, faster than 59.39% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(0)
        dummy.right = root
        res = []
        self.helper(root, res)
        for i in range(1, len(res)): #从1开始，避免最后新建一个多余的node.
            root.left = None
            root.right = TreeNode(res[i])
            root = root.right
        return dummy.right
        
    def helper(self, node, res):
        if not node:
            return 
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)
        
class Solution_2:
"""
Runtime: 40 ms, faster than 84.72% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.

Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)

这是真正的in-place,O(1)空间.
"""
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
    def __init__(self):
        self.prev = None