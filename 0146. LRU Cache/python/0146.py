class LRUCache_1:
"""
Runtime: 500 ms, faster than 12.73% of Python3 online submissions for LRU Cache.
Memory Usage: 22.8 MB, less than 6.06% of Python3 online submissions for LRU Cache.

这个方法不是O(1)的. 面试时如果对时间有要求不能写这个.
"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.dic = {}

    def get(self, key: int) -> int:
        if key in self.dic:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dic[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: #要先判断在不在，再判断大小够不够,否则会出问题.
            self.queue.remove(key)
            self.queue.append(key)
            self.dic[key] = value
            return
        if len(self.dic) >= self.capacity:
            k = self.queue.pop(0)
            self.dic.pop(k)
        self.queue.append(key)
        self.dic[key] = value
        
        class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache_2:
"""
Runtime: 256 ms, faster than 27.76% of Python3 online submissions for LRU Cache.
Memory Usage: 23.2 MB, less than 6.06% of Python3 online submissions for LRU Cache.

Link: https://leetcode.com/problems/lru-cache/discuss/202067/Python-or-O(1)-tm-146
https://www.youtube.com/watch?v=S6IfqDXWa10

第一个链接采用将新的node放在后面，而我的code是将新的node放在前面，和第二个视频链接一致。

这道题主要就是要知道双向链表的插入、删除操作的时间复杂度是O(1)的。
注意是双向，不是单向.单向链表的插入和删除是O(n)的。
"""
    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.insert(node)
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)   
        node = Node(key, value)
        self.insert(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity: #如果是先改value再判断大小，就只能判断是否大于.
            tail = self.dummy_tail.prev
            self.remove(tail)
            del self.dic[tail.key]
    """
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.insert(node)
            self.dic[key].val = value
            return 
        if len(self.dic) == self.capacity: #如果是先判断大小再改value,那么在判断大小之前的情况要及时return
            tail = self.dummy_tail.prev
            self.remove(tail)
            del self.dic[tail.key]
        node = Node(key, value)
        self.insert(node)
        self.dic[key] = node
        
    """    
    def insert(self, node):
        head = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = head
        head.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None