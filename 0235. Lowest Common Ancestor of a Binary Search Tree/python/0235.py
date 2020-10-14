class Solution_1:
"""
Runtime: 104 ms, faster than 20.31% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18 MB, less than 99.98% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

0236的解法可以直接拿来用，因为0236适用于所有二叉树
"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right
        
   
class Solution:
"""
Runtime: 80 ms, faster than 74.32% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18 MB, less than 99.98% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

但是因为本题是针对二叉搜索树，所以可以有简化
"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        