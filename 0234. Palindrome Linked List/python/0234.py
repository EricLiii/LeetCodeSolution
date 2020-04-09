class Solution_1:
"""
Runtime: 84 ms, faster than 39.40% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.3 MB, less than 7.69% of Python3 online submissions for Palindrome Linked List.

https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).

记这个!
"""
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # 这里可以只用node判断,但是不能只用head判断
        # 因为只用node可以handle输入链表长度为奇数的情况.
        # 但是只用head不行
        # 不过要注意,这个是在判断条件为while fast and fast.next的情况下才能用的.
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
        
class Solution_1_WRONG:
"""
注意：这个解法是不完整的。

这个解法看似和solution_1一样，其实要考虑的东西多得多。

"""
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow = fast = head
        # 这里如果是fast and fast.next(solotion_1),那么slow将会是后半链的第一个node.
        # 如果是fast.next and fast.next.next,slow将是前半链的最后一个node.
        # 因此solution_1中是将slow之后的倒序，而这个解法是将slow之前的倒序。
        
        # 这样判断不是不行，问题在于edge case更多了。
        # 例如input=[0,0],长度只有2,那么fast就一直没有移动,slow和fast一直指向相同的位置.
        # 因此需要在之前handle这个情况.
        
        # 另外,fast and fast.next还可以handle输入空链表的情况,
        # 而fast.next and fast.next.next需要额外判断.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt

            
        while fast and pre:
            if pre.val != fast.val:
                return False
            pre = pre.next
            fast = fast.next
        return False if pre or fast else True