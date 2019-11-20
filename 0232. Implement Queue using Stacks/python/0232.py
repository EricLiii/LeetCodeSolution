class MyQueue:
"""
Runtime: 52 ms, faster than 5.65% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Implement Queue using Stacks.

https://leetcode.com/problems/implement-queue-using-stacks/discuss/?currentPage=1&orderBy=most_posts&query=
太慢了，还有其他方法吗?
"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2)!= 0:
            return self.stack2.pop()
        else:
            while len(self.stack1)!= 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2)!= 0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!= 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0