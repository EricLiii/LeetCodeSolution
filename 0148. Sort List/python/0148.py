class Solution_1:
"""
Solution_1和solution_2思路完全一样，只是实现细节上有差别。
两个方法都采用了归并排序。
Link： https://blog.csdn.net/qq_35277038/article/details/83791342

Runtime: 236 ms, faster than 62.29% of Python3 online submissions for Sort List.
Memory Usage: 21.4 MB, less than 16.28% of Python3 online submissions for Sort List.
"""
    def def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        #这里只检查了fast和fast.next,所以在断开链表时要在slow之前断开。
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(*map(self.sortList, (head, slow)))
        
    def merge(self, h1, h2):
        # 只是创建一个空的节点，不算使用额外空间。
        dummy = head = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                head.next, head, h1 = h1, h1, h1.next
            else:
                head.next, head, h2 = h2, h2, h2.next
        head.next = h1 or h2
        return dummy.next
        
class Solution_2:
"""
Runtime: 224 ms, faster than 81.02% of Python3 online submissions for Sort List.
Memory Usage: 21.1 MB, less than 16.28% of Python3 online submissions for Sort List.

TODO: 时间复杂度为什么是nlog(n)呢？明明只做了一次对半分.
"""
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = fast = head
        #这里检查了fast.next和fast.next.next,所以在断开链表时要在slow之后断开。具体乐意自己画画图.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
        
    def merge(self, left, right):
        dummy = head = ListNode(None)
        while left and right:
            if left.val < right.val:
                head.next, head, left = left, left, left.next
            else:
                head.next, head, right = right, right, right.next 
        head.next = left or right
        return dummy.next