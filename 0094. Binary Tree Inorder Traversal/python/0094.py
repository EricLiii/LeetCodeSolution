# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
"""
Author: Zefeng

Runtime: 32 ms, faster than 92.66% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 5.24% of Python3 online submissions for Binary Tree Inorder Traversal.

Idea:
Recursive solution.
"""
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            #不要返回None，而是要返回[],否则最后的结果里包含None，是错误的。
            return [] 
        if not root.left and not root.right:
            return [root.val] #这里也记得要返回列表，而不仅仅是int。
        #这里由于两边返回的都是列表，所以中间也要列表化。
        res = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return res
        
class Solution_2:
"""
Runtime: 36 ms, faster than 72.14% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 5.24% of Python3 online submissions for Binary Tree Inorder Traversal.

Idea:
Link:https://www.cnblogs.com/grandyang/p/4297300.html

Use stack.
"""
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
            
class Solution_3:
"""
Morris Traversal!

Runtime: 40 ms, faster than 40.15% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.7 MB, less than 5.12% of Python3 online submissions for Binary Tree Inorder Traversal.

Idea:
Link: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
"""
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root != None:
            if root.left == None:
                res.append(root.val)
                root = root.right
            else:
                pre = root.left
                # 重点就是这里，判断条件要有两个，切记不能忘记pre.right!=root,
                # 否则会混淆pre.right为null和pre已经作为前序节点连接到后一节点的情况。
                while pre.right != None and pre.right != root:
                    pre = pre.right
                if pre.right == None:           
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None  # 恢复原输入数据
                    res.append(root.val)
                    root = root.right
        return res