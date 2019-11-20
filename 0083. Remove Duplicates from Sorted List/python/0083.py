# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_1:
"""
跟solution_2完全一样，是以前做的。
"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node=head
        while node and node.next:
            if (node.val==node.next.val):
                node.next=node.next.next
            else:
                node=node.next
        return head
        
class Solution_2:
"""
Author: Zefeng

Runtime: 48 ms, faster than 69.24% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 5.11% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next
        
class Solution_3:
"""
Runtime: 52 ms, faster than 34.86% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.8 MB, less than 5.11% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     
            cur = cur.next     
        return head
