class Solution:
"""
This question isn't easy to remember, try to do it for many times.

Runtime: 136 ms, faster than 95.74% of Python3 online submissions for Insertion Sort List.
Memory Usage: 15.7 MB, less than 13.89% of Python3 online submissions for Insertion Sort List.
"""
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            # 如果p.next.val > val, 说明cur.next的位置有可能在p之前，所以需要从头遍历。
            # 否则cur.next一定在p之后，不必从头遍历。
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next