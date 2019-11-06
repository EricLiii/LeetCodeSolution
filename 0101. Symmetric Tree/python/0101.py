# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
"""
Runtime: 44 ms, faster than 42.10% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.

递归.
"""
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left_node, right_node):
        if not left_node and not right_node: #and
            return True
        if not left_node or not right_node: #or
            return False
        if left_node.val != right_node.val:
            return False
        return self.is_mirror(right_node.right, left_node.left) and\
               self.is_mirror(left_node.right, right_node.left)
               
class Solution_2:
"""
Runtime: 40 ms, faster than 75.57% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.

迭代.
"""
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        dq = [(root.left,root.right)]
        while dq:
            node1, node2 = dq.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            # node1.left and node2.right are symmetric nodes in structure
            # node1.right and node2.left are symmetric nodes in structure
            dq.append((node1.left,node2.right))
            dq.append((node1.right,node2.left))
        return True
