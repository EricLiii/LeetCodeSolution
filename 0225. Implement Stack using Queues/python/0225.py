class MyStack_Wrong:
"""
Author: Zefeng

Runtime: 32 ms, faster than 89.38% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.7 MB, less than 20.00% of Python3 online submissions for Implement Stack using Queues.
"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.insert(0, x) #insert 是stack的操作，所以不能用!!!

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        output = self.queue[0]
        self.queue = self.queue[1:]
        return output
    
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return
        return self.queue[0]  

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False


class MyStack_1:
"""
Runtime: 36 ms, faster than 67.50% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Implement Stack using Queues.

"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
            
        return self.queue.pop(0)
    
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return
            
        #不能用self.queue[-1],这是stack的操作.
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        out = self.queue[0]
        self.queue.append(self.queue.pop(0))
        return out

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0