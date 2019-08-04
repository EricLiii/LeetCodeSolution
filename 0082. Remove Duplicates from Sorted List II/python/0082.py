class Solution_1:
"""
Runtime: 48 ms, faster than 69.42% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.8 MB, less than 5.62% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                #当时就是没想到如何处理若干连续节点的值相同的情况。
                #记住这个方法！
                #这里仅需判断head.next and head.val == head.next.val，无需判断head是否存在
                #   因为最外边已经保证head.next存在；
                #   而下面的head.next又保证了head=head.next之后的head是存在的。
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next