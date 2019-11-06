class Solution_1:
"""
Runtime: 36 ms, faster than 80.30% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.8 MB, less than 5.10% of Python3 online submissions for Reverse Linked List II.

Idea:
参考206. Reverse Linked List
"""
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(m-1):
            pre = pre.next
            head = head.next
        reverse = None
        for i in range(n-m+1):
            cur = head
            head = head.next #这里要先把head移开，再进行之后的操作.
            cur.next = reverse
            reverse = cur
        pre.next.next = head #这里要先指定pre.next.next,然后再指定pre.next
        pre.next = reverse
        return dummy.next
        
class Solution_2:
"""
Runtime: 28 ms, faster than 99.24% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Reverse Linked List II.

Idea:
避免了使用reverse。
"""
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        cur, prev = head, dummy
        for _ in range(m - 1):
            cur = cur.next
            prev = prev.next
        
        for _ in range(n - m): #其实就是每一次将cur的下一个放到pre的下一个，这样就完成了逆序.
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next