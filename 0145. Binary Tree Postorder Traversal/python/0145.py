

class Solution:
    # recursively 
    def postorderTraversal1(self, root):
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)

    # iteratively        
    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # 注意appendleft和right的顺序
                # 在preorder里是先append right再left，保证pop的时候先出left
                # 在postorder是先append left再right，保证pop的时候先出right，最后逆序才是postorder.
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []