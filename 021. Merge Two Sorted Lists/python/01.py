class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur=dummy=ListNode(0)
        while l1 and l2:  
            '''
            这里必须用and，因为如果用or的话：如果l1已经到达尾端，l2还有next，这时or判断仍为True，会继续执行判断if l1.val < l2.val。
            但此时l1已经是None了，不能l1.val，所以会报错。
            '''
            if l1.val < l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next
