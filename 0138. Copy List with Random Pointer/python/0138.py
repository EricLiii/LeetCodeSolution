"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution_1:
"""
Runtime: 40 ms, faster than 98.32% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 16.2 MB, less than 5.17% of Python3 online submissions for Copy List with Random Pointer.
"""
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next
        while n:
            #这里用get是因为n.next或者n.random可能为None.
            #这种情况下dic.get返回的就是None.
            #如果在while n: 之前执行dic[None] = None,下面就不用get了，直接dic[n.next]即可.
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
        
class Solution_2:
"""
很好的想法，值得学习！

Runtime: 44 ms, faster than 91.60% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 16.2 MB, less than 5.17% of Python3 online submissions for Copy List with Random Pointer.

Idea:
collections.defaultdict 的用法：https://www.cnblogs.com/zhizhan/p/5692668.html

"""
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = collections.defaultdict(lambda: Node(0, None, None)) #默认的Node为Node(0, None, None).
        dic[None] = None  #需要先指定key为None时的value,否则当next为None时，会生成一个新的Node，而不是指向None.
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]