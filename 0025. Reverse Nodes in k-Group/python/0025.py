class Solution:
"""
Runtime: 48 ms, faster than 91.51% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Reverse Nodes in k-Group.

https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/172576/Python-or-Follow-up-of-LC206
"""
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
        
        
class Solution_2:
"""
Runtime: 60 ms, faster than 11.18% of Python3 online submissions for Reverse Nodes in k-Group.

Zefeng
"""
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = ListNode()
        dummy = pre
        pre.next = head
        cur = head
        while cur:
            #判断是否有足够的nodes
            tmp = cur
            count = 0
            while tmp:
                count+= 1
                tmp = tmp.next
            if count < k:
                break
                
            for i in range(1, k):
                if cur.next:
                    nxt = cur.next
                    nnxt = nxt.next
                    pnxt = pre.next

                    pre.next = nxt
                    nxt.next = pnxt
                    cur.next = nnxt
            #记住要更新pre
            #而且是先更新pre,再更新cur。
            pre = cur
            cur = cur.next
        return dummy.next