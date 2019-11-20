class Solution_1:
"""
Runtime: 596 ms, faster than 5.06% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 37.6 MB, less than 5.55% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
https://segmentfault.com/a/1190000009429876
"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right
