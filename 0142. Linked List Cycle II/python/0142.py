class Solution(object)_1:
"""
This is a python2 solution.

Runtime: 36 ms, faster than 89.84% of Python online submissions for Linked List Cycle II.
Memory Usage: 18.1 MB, less than 74.79% of Python online submissions for Linked List Cycle II.

Idea: 
Link: https://leetcode.com/problems/linked-list-cycle-ii/discuss/345788/its-a-math-problem-specific-deduction-process
Link: https://www.cnblogs.com/grandyang/p/4137302.html

具体就是因为fast的速度是slow的两倍，所以当fast追上slow的时候，fast走过的距离是slow的两倍。
（注意，这个结论的前提是slow和fast在初始化时指向的是同一个ListNode。）

因为快指针每次走2，慢指针每次走1，快指针走的距离是慢指针的两倍。
而快指针又比慢指针多走了一圈。
所以head到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等。
现在重新开始，head运行到环起点 和 相遇点到环起点 的距离也是相等的， 相当于他们同时减掉了 环的起点到他们相遇的点的距离 
"""
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head