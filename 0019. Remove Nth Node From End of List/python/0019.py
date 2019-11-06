class Solution_1:
"""
Runtime: 40 ms, faster than 60.91% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Remove Nth Node From End of List.

Idea:
先将first和second的间隔找好，然后同时移动他俩就行。first作为哨兵去判断是否遍历到链表的尽头。
"""
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first, second = head, head
        for _ in range(n):
            first = first.next
        if not first: #说明要移走的是正序第一个node.
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
   
class Solution_2:
"""
Runtime: 36 ms, faster than 86.64% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Remove Nth Node From End of List.

Idea:
思路就是用remove（）函数将链表分解，然后从链表末尾倒着往回找n个node。一旦找到倒数第n+1个node，就断开倒数第n个node。
"""
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:   
        def remove(node):
            if not node:
                return 0
            i = remove(node.next) + 1
            if i == n+1: #如果是要去掉第一个node，i永远不会等于n+1，所以不会有冲突。
                node.next = node.next.next
            return i
         
        count = remove(head)
        if count == n:
            return head.next
        return head
        
class Solution_3:
"""
Runtime: 40 ms, faster than 60.91% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Remove Nth Node From End of List.

Idea:
改变值，而不是移动node。
"""
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
