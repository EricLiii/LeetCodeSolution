class Solution_1:
"""
Runtime: 60 ms, faster than 64.86% of Python3 online submissions for Unique Binary Search Trees II.
Memory Usage: 15.6 MB, less than 6.67% of Python3 online submissions for Unique Binary Search Trees II.
"""
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n+1)
         
    def helper(self, start, end):
        #注意返回条件是相等.
        if start == end:
            #这里返回[None]是因为可能没有左(右)子树,即左(右)子树为None.
            #但是返回None的话不能进行遍历，所以要返回[None].
            return [None]
        res = []
        for i in range(start, end):
            left = self.helper(start, i)
            right = self.helper(i+1, end)
            for m in left:
                for n in right:
                    node = TreeNode(i)
                    node.left = m
                    node.right = n
                    res.append(node)
        return res