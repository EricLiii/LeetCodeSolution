class MinStack_1:
"""
Runtime: 76 ms, faster than 52.58% of Python3 online submissions for Min Stack.
Memory Usage: 17.9 MB, less than 5.36% of Python3 online submissions for Min Stack.
"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        #利用getMin初始化curMin,避免了用最小int值初始化getMin,值得学习!
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin));

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
            
class MinStack_2:
"""
Runtime: 72 ms, faster than 75.22% of Python3 online submissions for Min Stack.
Memory Usage: 17.2 MB, less than 8.93% of Python3 online submissions for Min Stack.

Link: https://leetcode.com/problems/min-stack/discuss/49014/Java-accepted-solution-using-one-stack
Link: https://www.cnblogs.com/lightwindy/p/8512214.html
"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")

    def push(self, x: int) -> None:
        if x <= self.min:
            #这时x是新的最小值,因此先在stack末尾加一个当前最小值，作为最近的旧的最小值的备份.
            #将x设为当前最小值.
            #当调用pop后弹出的是当前最小值时，stack会再弹出一个值。
            #而这个值就是最近的旧的最小值，将其设为当前最小值.
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        #有两次pop(),执行完pop(self)函数后stack总共弹出两个成员.
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min