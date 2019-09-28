class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 46.39% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 5.14% of Python3 online submissions for Swap Nodes in Pairs.
"""
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        dummy = pre
        while head and head.next:
            a = head.next
            b = head.next.next
            c = head
            pre.next = a
            pre.next.next = c
            c.next = b
            pre = pre.next.next
            head = pre.next
        return dummy.next
        
class Solution_2:
"""
Runtime: 40 ms, faster than 46.39% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 5.14% of Python3 online submissions for Swap Nodes in Pairs.

Idea:
Same idea with solution_1, but more concise.
"""
    def swapPairs(self, head: ListNode) -> ListNode:
        # self在这里的用法： （个人理解，不一定对）
        # 可以去看leetcode里playground的具体代码。main()函数会创建一个solution的实例。
        # self其实就指向这个实例。
        # 由于这个类在调用swapPairs之后返回的是一个ListNode，所以self也是一个ListNode。
        # 所以可以这样初始化pre。
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
        
class Solution_3:
"""
Runtime: 36 ms, faster than 77.71% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 5.14% of Python3 online submissions for Swap Nodes in Pairs.

Idea:
跟solution_2一样，只不过没用self。
"""
    def swapPairs(self, head: ListNode) -> ListNode:
        # 这里注意，dummy = ListNode(0)    和     dummy = pre = ListNode(0)      
        #           pre = ListNode(0)
        # 这两种写法代表的含义是不一样的.
        # 第一种：dummy和pre指向的是同一个空间，对pre的操作也是对dummy的操作;
        # 第二种：dummy和pre是独立的,开辟了两个空间，对pre的操作不影响dummy;
        # 这是因为第二种里dummy和pre是对同一个ListNode的引用.
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next