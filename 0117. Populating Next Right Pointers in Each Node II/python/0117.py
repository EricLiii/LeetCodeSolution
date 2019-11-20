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