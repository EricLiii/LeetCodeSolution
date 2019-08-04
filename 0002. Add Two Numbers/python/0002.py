def addTwoNumbers(self, l1, l2):
"""
Runtime: 80 ms, faster than 56.03% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.13% of Python3 online submissions for Add Two Numbers.
"""
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next
    
class Solution:
"""
Author: Zefeng

Runtime: 76 ms, faster than 78.39% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 5.13% of Python3 online submissions for Add Two Numbers.
"""
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = head = ListNode(0)
        dummy.next = head
        while l1 or l2 or carry:
            if not l1 and not l2 and carry:
                head.next = ListNode(carry)
                break
            if l1 and l2:
                summ = l1.val + l2.val +carry
                if summ > 9:
                    summ = summ - 10
                    carry = 1
                else:
                    carry = 0
                head.next = ListNode(summ)
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                summ = l1.val + carry
                if summ > 9:
                    summ = summ -10
                    carry = 1
                else:
                    carry = 0
                head.next = ListNode(summ)
                l1 = l1.next
            else:
                summ = l2.val + carry
                if summ > 9:
                    summ = summ -10
                    carry = 1
                else:
                    carry = 0
                l2 = l2.next
                head.next = ListNode(summ)
            head = head.next
        return dummy.next
        
class Solution_3:
"""
Runtime: 76 ms, faster than 78.39% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 5.13% of Python3 online submissions for Add Two Numbers.
"""
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10) # Remember the usage of divmod.
            n.next = ListNode(val)
            n = n.next
        return root.next
