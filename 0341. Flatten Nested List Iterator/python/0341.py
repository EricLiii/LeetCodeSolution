class NestedIterator:
"""
Runtime: 72 ms, faster than 38.31% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Flatten Nested List Iterator.

https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80142/8-line-Python-Solution
"""
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # 如果pop出的不是int, getInteger会返回None
        # 但是这种情况是不会出现的,因为在调用next()之前已经调用hasNext()了.
        # 而在hasNext中对是否为int做出了判断,并进行处理.
        # 从而保证了next()中当hasNext时pop出来的一定是int.
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False