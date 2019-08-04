class Solution_1:
"""
Author: Zefeng

Runtime: 36 ms, faster than 90.79% of Python3 online submissions for Partition List.
Memory Usage: 13.7 MB, less than 5.09% of Python3 online submissions for Partition List.
"""
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = smaller = ListNode(0)
        dummy2 = larger = ListNode(0)
        while head:
            if head.val >= x:
                larger.next = ListNode(head.val)
                larger = larger.next
            else:
                smaller.next = ListNode(head.val)
                smaller = smaller.next
            head = head.next
        smaller.next = dummy2.next
        return dummy1.next