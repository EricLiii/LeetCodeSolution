class Solution:
"""
Runtime: 100 ms, faster than 55.17% of Python3 online submissions for Reorder List.
Memory Usage: 22.3 MB, less than 7.69% of Python3 online submissions for Reorder List.

Idea:
1.先找中点，然后分成两个部分。
2.对后面的部分进行倒序排列。
3.将第二个链表穿插到第一个中。
"""
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        pre = None
        #也可以:
        #while mid:
        #   cur = mid
        #   mid, cur.next, pre = mid.next, pre, cur
        while mid:
            cur = mid
            mid = mid.next
            cur.next = pre
            pre = cur
            
        # 可以去尝试，无论总链表长度为奇数还是偶数，以上述方法找中点并分开后，第一部分的长度总是大于或等于第二部分。
        # 也就是说，只有可能pre先于head为空，不可能head为空，pre还有。
        # 同时head最多也只能比pre多一个节点。
        # 所以这里只要检查pre是否为空就行。
        while pre:
            #不能这样写:head.next, pre, head.next.next, head = pre, pre.next, head.next, head.next.next
            #因为在进行处理之前python会先提取等号右边的值
            #而head.next.next = None (以输入1-2-3-4为例).
            #如果一步一步来,head.next.next其实不是None.
            #这样就产生了错误.
            #上面的while mid不会有这样的问题.
        #参考:https://blog.csdn.net/u014745194/article/details/72782962
        # https://leetcode.com/problems/reorder-list/discuss/44988/A-python-solution-O(n)-time-O(1)-space
        
            #但是以后做连续赋值的时候应该如果取决用哪个呢? 有时间好好想一想.
            tmp = head.next
            head.next = pre
            pre = pre.next
            head.next.next = tmp
            head = head.next.next