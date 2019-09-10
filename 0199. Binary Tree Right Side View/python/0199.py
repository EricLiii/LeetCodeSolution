class Solution_1:
"""
Runtime: 32 ms, faster than 96.70% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.

递归.
思路是先层序遍历，然后打印出每行末尾的数字。虽然能行但是太蠢了。
"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.sol = [[]]
        self.helper(root, 1)
        res = []
        for item in self.sol[:-1]:
            res.append(item[-1])
        return res
    
    def helper(self, node, level):
        if not node:
            return
        else:
            self.sol[level-1].append(node.val)
            if len(self.sol) == level:
                self.sol.append([])
            self.helper(node.left, level+1)
            self.helper(node.right, level+1)
            
class Solution_2:
"""
Runtime: 40 ms, faster than 59.96% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.

和solution_1一样，但是处理过程中就更新sol，避免了最后还要通过遍历来找末尾元素.
"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.sol = [[]]
        self.helper(root, 1)
        return self.sol[:-1]
    
    def helper(self, node, level):
        if not node:
            return
        else:
            self.sol[level-1] = node.val #直接更新sol.
            if len(self.sol) == level:
                self.sol.append([])
            self.helper(node.left, level+1)
            self.helper(node.right, level+1)
            
class Solution_3:
"""
Runtime: 40 ms, faster than 59.96% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.

Link: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56203/Simple-C%2B%2B-solution-(BTW%3A-I-like-clean-codes)

更简洁的dfs.
"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, node, level, res):
        if not node:
            return
        if level >= len(res):
            res.append(node.val)
        self.dfs(node.right, level+1, res) #一定是先右后左，保证right view.
        self.dfs(node.left, level+1, res)       
        
class Solution_4:
"""
Runtime: 36 ms, faster than 85.79% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.

Link: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

迭代
"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view