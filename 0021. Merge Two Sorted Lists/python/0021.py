class Uncomplished_Solution:
"""
当时卡住的code。
"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(0)
        dummy.next = head
        while l1 and l2:
            if l1.val >= l2.val:
                head.val = l2.val
                l2 = l2.next
            elif l1.val < l2.val:
                head.val = l1.val
                l1 = l1.next
            # 当时就是卡在这里，当l1或者l2为None时，会额外多加一个Node。
            # 解决办法参考solution_1。
            head.next = ListNode(0)
        if l1:
            pass
        elif l2:
            pass
        return dummy.next

class Solution_1:
"""
Runtime: 40 ms, faster than 88.29% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 5.24% of Python3 online submissions for Merge Two Sorted Lists.

Idea: 
Iteratively.
"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy = ListNode(0) #解决办法在这里.
        while l1 and l2:  
            '''
            这里必须用and，因为如果用or的话：如果l1已经到达尾端，l2还有next，这时or判断仍为True，会继续执行判断if l1.val < l2.val。
            但此时l1已经是None了，不能l1.val，所以会报错。
            '''
            if l1.val < l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2 #这个语法值得学习。
        return dummy.next
        
class Solution_2:
"""
Runtime: 44 ms, faster than 65.23% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.7 MB, less than 5.24% of Python3 online submissions for Merge Two Sorted Lists.

Idea:
Recursively. No need to allocate extra space.
"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
         
class Solution_3:
"""
Runtime: 44 ms, faster than 65.23% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.1 MB, less than 5.24% of Python3 online submissions for Merge Two Sorted Lists.

Idea:
Iteratively. But in-place.
"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
class Solution_4:
"""
Author: Zefeng

Runtime: 44 ms, faster than 64.21% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.6 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                l1 = l1.next
            head = head.next
        if l1 or l2:
            head.next = l1 or l2
        return dummy.next