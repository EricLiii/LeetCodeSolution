# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]
    
    def inorder(self, node, depth, traversal):
        if not node:
            return
        if len(traversal) == depth:
            traversal.append([])
        self.inorder(node.left, depth+1, traversal)
        traversal[depth].append(node.val)
        self.inorder(node.right, depth+1, traversal)
        
class Solution_2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)
