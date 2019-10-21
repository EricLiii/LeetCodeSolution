class Solution:
"""
Runtime: 84 ms, faster than 39.40% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.3 MB, less than 7.69% of Python3 online submissions for Palindrome Linked List.

https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).

"""
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True