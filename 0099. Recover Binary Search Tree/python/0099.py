class Solution_1:
"""
Recover Binary Search Tree.
Memory Usage: 14.7 MB, less than 21.77% of Python3 online submissions for Recover Binary Search Tree.

https://blog.csdn.net/zhangxiao93/article/details/50933482

https://www.cnblogs.com/anniekim/archive/2013/06/15/morristraversal.html

https://leetcode.com/problems/recover-binary-search-tree/discuss/917430/Python-O(n)O(1)-Morris-traversal-explained
"""
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, node, cands = root, TreeNode(-float("inf")), []
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if cur.val < node.val:
                        cands += [node, cur]
                    node = cur
                    cur = cur.right
            else:
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right
            
        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val