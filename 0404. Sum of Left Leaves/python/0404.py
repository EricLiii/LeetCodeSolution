class Solution_1:
"""
Runtime: 32 ms, faster than 72.94% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.4 MB, less than 30.47% of Python3 online submissions for Sum of Left Leaves.

iteration
https://leetcode.com/problems/sum-of-left-leaves/discuss/292953/Python-iterative-solution-beats-

注意如果只有root，root不算leaf
"""
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, False)]
        while stack:
            curr, is_left = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if is_left:
                    result += curr.val
            else:
                stack.append((curr.left, True))
                stack.append((curr.right, False))
        return result
        
class Solution_2:
"""
Runtime: 28 ms, faster than 91.14% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.7 MB, less than 30.47% of Python3 online submissions for Sum of Left Leaves.

https://leetcode.com/problems/sum-of-left-leaves/discuss/88977/4-Lines-Python-Recursive-AC-Solution
dfs
"""
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)