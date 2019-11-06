class BSTIterator_1:
"""
Runtime: 84 ms, faster than 91.14% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.8 MB, less than 7.69% of Python3 online submissions for Binary Search Tree Iterator.

Link: https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator
"""
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0