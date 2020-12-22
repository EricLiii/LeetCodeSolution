class Solution_1:
"""
Runtime: 132 ms, faster than 70.27% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16.6 MB, less than 42.26% of Python3 online submissions for Insert into a Binary Search Tree.

https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/180244/Python-4-line-clean-recursive-solution
"""
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: 
            return TreeNode(val)
        if root.val < val: 
            root.right = self.insertIntoBST(root.right, val)
        else: 
            root.left = self.insertIntoBST(root.left, val)
        return root