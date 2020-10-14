

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
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []