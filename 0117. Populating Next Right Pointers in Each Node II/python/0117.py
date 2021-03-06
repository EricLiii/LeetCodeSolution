class Solution_1:
"""
Runtime: 396 ms, faster than 48.16% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 48.4 MB, less than 8.33% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

Link: https://www.cnblogs.com/grandyang/p/4288151.html

迭代. but not constant extra space. 但是同样适用于0116.
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
        
class Solution_2:
"""
Runtime: 396 ms, faster than 48.16% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 48.5 MB, less than 8.33% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand

Constant extra space.
"""
    def connect(self, root: 'Node') -> 'Node':
        head = Node(0)
        head.next = root
        #开始时tail和dummy指向同一位置p，随着对tail的操作，p的属性也会变化，但是dummy仍然指向起始位置.
        tail = dummy = Node(0) 
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next
        return head.next


class Solution_3:
"""
Runtime: 396 ms, faster than 55.05% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 49.7 MB, less than 8.33% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37811/Simple-solution-using-constant-space

记这个，更清晰。
"""
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0)
        dummy.next = root
        while root:
            tmp = Node(0)
            cur = tmp
            while root:
                if root.left:
                    cur.next = root.left # 当cur和tmp还是指向同一node的时候，此行或下行会将tmp指向root的下一层的node（如果有）
                    cur = cur.next
                if root.right:
                    cur.next = root.right # 当cur和tmp还是指向同一node的时候，此行或上行会将tmp指向root的下一层的node（如果有）
                    cur = cur.next
                root = root.next
            root = tmp.next #tmp指向的是root的下一层的第一个node.
        return dummy.next
        
class Solution_4:
"""
Runtime: 64 ms, faster than 15.75% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

对solution_3进行了改写，使其更易懂.
但是记最好还是记solution_3.
"""
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0)
        dummy.next = root
        while root:
            start = Node(0)
            found_start = False
            cur = start
            while root:
                if root.left:
                    cur.next = root.left 
                    if not found_start:
                        start = cur 
                        found_start = True
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    if not found_start:
                        start = cur 
                        found_start = True
                    cur = cur.next
                root = root.next
            root = start.next 
        return dummy.next
