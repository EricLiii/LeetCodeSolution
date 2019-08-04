class Solution:
"""

Idea:
1.先找中点，然后分成两个部分。
2.对后面的部分进行倒序排列。
3.将第二个链表穿插到第一个中。
"""
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        pre = None
        while mid:
            cur = mid
            mid = mid.next
            cur.next = pre
            pre = cur
            
        # 可以去尝试，无论总链表长度为奇数还是偶数，以上述方法找中点并分开后，第一部分的长度总是大于或等于第二部分。
        # 也就是说，只有可能pre先于head为空，不可能head为空，pre还有。
        # 同时head最多也只能比pre多一个节点。
        # 所以这里只要检查pre是否为空就行。
        while pre:
            tmp = head.next
            head.next = pre
            pre = pre.next
            head.next.next = tmp
            head = head.next.next