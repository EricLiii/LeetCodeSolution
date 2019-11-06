class Solution(object)_1:
"""
This is a python2 solution.

Runtime: 40 ms, faster than 62.88% of Python online submissions for Linked List Cycle.
Memory Usage: 18.1 MB, less than 84.18% of Python online submissions for Linked List Cycle.
"""
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            #这里要先让slow和fast跑起来再去进行判断，因为slow和fast初始化的时候是相等的。另见solution_2.
            if slow is fast:  #slow is fast 和 slow == fast 都可以，但是最好用is，因为这是python。
                return True
        return False
        
class Solution(object)_2:
    def hasCycle(self, head):
        #如果slow和fast以下面的方式初始化，则要考虑head为空的情况。
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next and fast.next.next:
            # 这里就可以先做判断了，因为初始化不一样了。
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False     