class Solution_1:
"""
Runtime: 56 ms, faster than 61.58% of Python3 online submissions for Path Sum II.
Memory Usage: 19 MB, less than 6.90% of Python3 online submissions for Path Sum II.

dfs
"""
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: 
            return []
        self.res = []
        self.find(root, sum, [])
        return self.res
        
    def find(self, node, sum, path):
        if not node:
            return 
        if not node.left and not node.right and node.val == sum:
            self.res.append(path + [node.val])
        sum -= node.val
        self.find(node.left, sum, path + [node.val]) 
        self.find(node.right, sum, path + [node.val])
        
class Solution_2:
"""
Runtime: 48 ms, faster than 95.25% of Python3 online submissions for Path Sum II.
Memory Usage: 15.2 MB, less than 37.93% of Python3 online submissions for Path Sum II.

bfs + queue
"""
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, path = queue.pop(0) #从0处pop，所以是bfs.
            if not curr.left and not curr.right and val == sum:
                res.append(path)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, path+[curr.left.val])) #val加
            if curr.right:
                queue.append((curr.right, val+curr.right.val, path+[curr.right.val]))
        return res
        
class Solution_3:
"""
Runtime: 56 ms, faster than 61.58% of Python3 online submissions for Path Sum II.
Memory Usage: 14.6 MB, less than 93.10% of Python3 online submissions for Path Sum II.

dfs + stack
"""
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop() #从末尾pop，所以是dfs.
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right: #先左先右没关系.
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val])) #val减
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 