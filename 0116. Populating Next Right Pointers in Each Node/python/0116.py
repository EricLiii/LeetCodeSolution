class Solution_1:
"""
Runtime: 64 ms, faster than 92.36% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.8 MB, less than 7.14% of Python3 online submissions for Populating Next Right Pointers in Each Node.

Link: https://www.cnblogs.com/grandyang/p/4288151.html

递归.
"""
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
        return root
        
class Solution_2:
"""
Runtime: 68 ms, faster than 75.64% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Populating Next Right Pointers in Each Node.

Link: https://www.cnblogs.com/grandyang/p/4288151.html

迭代. but not constant extra space. 但是同样适用于0117.

不要记这个!
"""
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = []
        queue.append(root)
        while queue:
            siz = len(queue) #要先算出大小，后面的pop会改变大小.
            for i in range(siz):
                node = queue.pop(0)
                if i < siz-1:
                    node.next = queue[0] #因为每个node的next初始值都是None，所以不用考虑如何给root。next赋值.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        
class Solution_2_Improve:
"""
Runtime: 64 ms, faster than 64.69% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.4 MB, less than 35.71% of Python3 online submissions for Populating Next Right Pointers in Each Node.

其实Solution_2不用计算siz
但是仍然不是constant space, 不要记这个!
"""
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                node.left.next = node.right
                stack.append(node.left)
            if node.right:
                node.right.next = node.next.left if node.next else None
                stack.append(node.right)
        return root
        
        
class Solution_3:
"""
Runtime: 64 ms, faster than 92.36% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Populating Next Right Pointers in Each Node.

Link: https://www.cnblogs.com/grandyang/p/4288151.html

用两个指针
"""
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        start = root
        while start.left:
            cur = start
            while cur: #这个while是先将每一层都连接好，然后用start=start.left跳到下一层.
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
        return root
        
class Solution_4:
"""
Runtime: 64 ms, faster than 64.69% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.4 MB, less than 35.71% of Python3 online submissions for Populating Next Right Pointers in Each Node.

记solution3或者4
"""
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left
        return root
