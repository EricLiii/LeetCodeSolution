class Solution(object)_1:
"""
Runtime: 188 ms, faster than 83.94% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.7 MB, less than 88.29% of Python online submissions for Intersection of Two Linked Lists.

Idea:
查找两个链表的共同节点
要求：时间复杂度为 O(N)，空间复杂度为 O(1)

设 A 的长度为 a + c， B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。

当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；
同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。

这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点


记这个!!!
"""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA 
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa 
        
class Solution(object)_2:
"""
Runtime: 208 ms, faster than 27.44% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.7 MB, less than 83.78% of Python online submissions for Intersection of Two Linked Lists.

Idea:
Concatenate list A and list B, if there's an intersection, there's loop, so we need to find the start of the loop if there's any.

其实就是将本题转化为'142. Linked List Cycle II'.
"""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: 
            return None
        last = headA
        while last.next: 
            last = last.next
        last.next = headB
        fast = slow = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow
        last.next = None
        return None