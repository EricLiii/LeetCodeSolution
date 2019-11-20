class Solution_1:
"""
Author: Zefeng

Runtime: 60 ms, faster than 67.75% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 17.8 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.
"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        stack = []
        while root:
            stack.append(root)
            root = root.left
        count = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            count += 1
            if count == k:
                return node.val
            else:
                stack.append(node.right)
                node_ = stack[-1]
                while node_:
                    stack.append(node_.left)
                    node_ = node_.left
        return None

class Solution_2:
"""
Runtime: 60 ms, faster than 67.75% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 17.9 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.

和solution_1思路一样，但是更简洁。
"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


class Solution_3:
"""
Runtime: 48 ms, faster than 98.91% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.

recursively.

https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
	#self.flag is used to record if we have find the target value.
	#the code in link doesn't have this flag, I add it by myself and improve time complexity from lower tha 50% to more than 95%.
        self.found = False
        self.helper(root)
        return self.res

    def helper(self, node):
	# if we have found the target value, exit in good time.
        if self.found:
            return
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            self.found = True
            return
        self.helper(node.right)
