class Solution:
"""
Runtime: 56 ms, faster than 38.60% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 16.1 MB, less than 8.11% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left==None or root.right==None:
            #这块是精华.
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1