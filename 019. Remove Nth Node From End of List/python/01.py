class Solution:
    '''
    52ms
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first, second = head, head
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
   
   
   
class Solution:
    '''
    faster, 40ms
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:   
        def remove(node):
            if not node:
                return 0
            i = remove(node.next) + 1
            if i == n+1:
                node.next = node.next.next
            return i
         
        count = remove(head)
        if count == n:
            return head.next
        return head
