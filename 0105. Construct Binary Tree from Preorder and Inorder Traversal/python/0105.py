# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
"""
Author: Zefeng

Runtime: 516 ms, faster than 5.03% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 89 MB, less than 5.11% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

Very slow! Read comment.
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and inorder:
            root = TreeNode(inorder[0])
            return root
        if preorder and not inorder:
            return None
        # 以上判断是累赘的。因为不可能有preorder为空，同时inorder不为空的情况。只可能有inorder为空同时preorder不为空的情况。
        # 所以只需要判断inorder就可以了。
        for i in range(len(preorder)):
            #两个for循环也是没有必要的：
            #  1.首先preorder的首个元素一定是root。
            #  2。其次，我在这里用两个for是因为在后面递归时，我没有in-place修改preorder，只是传递了preorder在i后面的部分。
            #    这个部分包含了preorder中以当前root为root的左右子树。在下一次递归中需要遍历传递的preorder来找到下一个root。
            #    这样就造成了多余的运算。
            #  3.可以用pop()来in-place修改preorder，这样就保证了每次传递到下一递归的preorder的第一个元素一定是root。
            for j in range(len(inorder)):
                if inorder[j] == preorder[i]:
                    root = TreeNode(preorder[i])  # 初始化一个TreeNode的方法记住，不能直接TtreeNode.val=preorder[i].
                    root.val = preorder[i]
                    root.left = self.buildTree(preorder[i+1:], inorder[:j])
                    root.right = self.buildTree(preorder[i+1:], inorder[j+1:])
                    return root
        return None # 在这个题中，貌似没有可能preorder和inorder的元素完全不相同，所以或许是没必要的。


class Solution_2:
"""
Runtime: 132 ms, faster than 61.55% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.9 MB, less than 41.56% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

Improved solution_1 according to comments. But still can be improved.

记这个!!

IMPORTANT: 其实，这个题的重点是题中说明了没有重复数字出现。因此我们才能直接将preorder[1:]代入下一个递归，让下一个递归排除掉preorder中多余的元素。
如果包含重复数字，本txt中的所有方法都是错的!!!!
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0)) 
            # 这里慢的原因是因为pop(0)操作会从preorder末尾开始遍历，直到到达preorder的第一个元素，并将其pop（）
            # 这样的话每一次pop(0)的时间复杂度都是O(n)
            # 如果在开始就将preorder和inorder进行reverse()，虽然两次reverse()的时间复杂度也是O(n)，但是之后只需要pop(),而不是pop(0)
            # 这样算法就快很多了.详情见Solution_3.
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            #这里可以直接用preorder的原因是：在上一行里，preorder已经做过pop(0)了，
            #所以下一行的preorder[0]一定存在于inorder.
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

class Solution_3:
"""
Runtime: 100 ms, faster than 71.68% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.7 MB, less than 42.64% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse() # reverse()是in-place操作。
        inorder.reverse()
        return self.build(preorder, inorder)
        
    def build(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop()) 
            root = TreeNode(inorder[ind])
            root.left = self.build(preorder, inorder[ind+1:])
            root.right = self.build(preorder, inorder[:ind])
            return root
            
class Solution_4:
"""
Runtime: 60 ms, faster than 79.47% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 14.7 MB, less than 95.71% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

Idea:
Iterate solution. Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!

这个实现不太简明，以后有时间改进一下!

Idea: 
  Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
  Process: ( N(x,l,r) means N.val=x, N.left=l, N.right=r. ) 
        pre       ino         prev              curr              stack                                    
        -----------------------------------------------------------------------------------------
        1         0                                               N(3,null,null)
        -----------------------------------------------------------------------------------------
        1->2      0           None              N(9,null,null)    N(3,9,null), N(9,null,null)
        -----------------------------------------------------------------------------------------
        2->3      0->1        N(9,null,null)    N(20,null,null)   N(3,9,null)
                  1->2        N(3,9,null)       N(20,null,null)   []
                              N(3,9,20)         N(20,null,null)   N(20,null,null)
        -----------------------------------------------------------------------------------------
        3->4      2           None              N(15,null,null)   N(20,15,null), N(15,null,null)
        -----------------------------------------------------------------------------------------
        4->5      2->3        N(15,null,null)   N(7,null,null)    N(20,15,null)      
                  3->4        N(20,15,null)     N(7,null,null)    []
                              N(20,15,7)        N(7,null,null)    N(7,null,null)   
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        
        pre = 1
        ino = 0
        while (pre < len(preorder)):
            curr = TreeNode(preorder[pre])
            pre += 1
            prev = None
            # 以下的原理就是，当前序排列读到中序排列的起点时，说明在前序中已经走到最左边的叶。
            # 此时需要通过回溯来添加之前的节点的右子树。
            while stack and stack[-1].val == inorder[ino]:
                #这里要注意，每次pop()之后，stack的最后一个元素弹出，同时ino也会加1.
                #这样就导致stack有可能一直弹出,直到打破while循环(即来到一个存在右子叶的节点)。
                prev = stack.pop()
                ino += 1
            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr 
            stack.append(curr)
        return root
        
class Solution_5:
"""
Author: Zefeng

Runtime: 456 ms, faster than 8.37% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.5 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

太慢了.
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and inorder:
            return 
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root = TreeNode(preorder[0])
                root.left = self.buildTree(preorder[1:], inorder[:i])
                root.right = self.buildTree(preorder[len(inorder[:i])+1:], inorder[i+1:])
                return root
        return None