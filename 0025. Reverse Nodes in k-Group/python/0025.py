class Solution:
"""
Runtime: 48 ms, faster than 91.51% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Reverse Nodes in k-Group.

https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/172576/Python-or-Follow-up-of-LC206
"""
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)