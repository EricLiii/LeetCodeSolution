class Solution_1:
"""
Runtime: 44 ms, faster than 90.80% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.

https://leetcode.com/problems/odd-even-linked-list/discuss/78095/Clear-Python-Solution
"""
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
