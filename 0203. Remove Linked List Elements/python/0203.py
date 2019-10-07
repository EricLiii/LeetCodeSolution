class Solution_1:
"""
Author: Zefeng

Runtime: 72 ms, faster than 87.72% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 16.9 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
"""
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = None #或者pre.next = head.next,这样似乎更好。
                head = head.next
                continue
            else:
                pre.next = head
                pre = head
                head = head.next
        return dummy.next