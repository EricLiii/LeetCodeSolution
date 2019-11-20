class Solution_1:
"""
Author: Zefeng

Runtime: 44 ms, faster than 60.22% of Python3 online submissions for Rotate List.
Memory Usage: 13.9 MB, less than 5.45% of Python3 online submissions for Rotate List.

Idea: 
将链表变成环，然后寻找断开的位置。
"""
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        tmp = head
        n = 1  #已经排除了head为空的情况，所以要从1开始。
        while tmp.next:
            tmp = tmp.next
            n += 1
        tmp.next = head
        pos = n - k%n
        for _ in range(pos-1):
            head = head.next
        res = head.next
        head.next = None
        return res