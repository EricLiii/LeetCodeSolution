class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 57.55% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.
"""
    def sumNumbers(self, root: TreeNode) -> int:
        self.summ = 0
        #这里既然已经将summ设为self，就没有必要代入函数了.
        #所以直接self.helper(root, [])即可. 见solution_4.
        self.helper(root, [], self.summ)
        return self.summ
    
    def helper(self, node, path, summ):
        if not node:
            return
        if not node.left and not node.right:
            path = "".join(path + [str(node.val)])
            self.summ += int(path)
        if node.left:
            self.helper(node.left, path + [str(node.val)], self.summ)
        if node.right:
            self.helper(node.right, path + [str(node.val)], self.summ)
            
class Solution_2:
"""
Runtime: 36 ms, faster than 87.11% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.

和solution_1一样，但是避免了int和string的转换，递归法记这个!
"""
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value*10+root.val)
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val
                
class Solution_3:
"""
Runtime: 36 ms, faster than 87.11% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.

dfs + stack
"""
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, root.val)], 0 #当时没想到stack里放set这个技巧.
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res
        
class Solution_4:
"""
Author: Zefeng

Runtime: 36 ms, faster than 86.18% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers
"""
    def sumNumbers(self, root: TreeNode) -> int:
        #注意！！！
        #这里必须将summ设为self。因为summ是int，属于静态变量。
        #如果summ不是self,self.dfs(root, [], summ)中不会引用summ，而是copy一个新的summ。
        #所以在return summ中，summ还是0.
        self.summ = 0
        self.dfs(root, [])
        return self.summ
    
    def dfs(self, root, path):
        if not root: #这一步不要忘了，最初的输入有可能为None.
            return
        if not root.left and not root.right:
            path += [root.val]
            tmp = "".join(list(map(str, path)))
            self.summ += int(tmp)
            return
        if root.left:
            self.dfs(root.left, path + [root.val])
        if root.right:
            self.dfs(root.right, path + [root.val])