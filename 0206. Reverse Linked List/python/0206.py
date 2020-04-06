class Solution_WRONG:
"""
Zefeng
"""

    def reverseList(self, head: ListNode) -> ListNode:
        if head and head.next:
            nxt = head.next
            #这里出错! head.next应该是prev.
            #如果一直head.next=None,中间就没有连起来.
            head.next = None 
            tmp = self.reverseList(nxt)
   
            tmp.next = head
            return tmp

        else:
            return head

class Solution_1:
"""
Runtime: 32 ms, faster than 81.19% of Python3 online submissions for Reverse Linked List.
Memory Usage: 18.5 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.

recursive
"""
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head, None)

    def helper(self, head, prev):
        if not head:
            return prev
        curr, head.next = head.next, prev
        return self.helper(curr, head)
        
        
class Solution_2:
"""
Runtime: 32 ms, faster than 81.19% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.

Iterative
"""
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head.next
            head.next = prev
            prev = head
            head = cur
        return prev