class Solution_1:
"""
Author: Zefeng

Runtime: 44 ms, faster than 46.46% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Happy Number.
"""
    def isHappy(self, n: int) -> bool:
        self.lst = []
        return self.helper(n)
    
    def helper(self, n):
        if n == 1:
            return True
        summ = 0
        while n:
            summ += (n % 10)**2
            n = n // 10
        if summ in self.lst:
            return False
        else:
            self.lst.append(summ)
        return self.helper(summ)
        
class Solution_2:
"""
Runtime: 44 ms, faster than 46.46% of Python3 online submissions for Happy Number.
Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Happy Number.

更简洁，不需要定义新的函数.
"""
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem: #说明已经形成loop,但是不是以1为结尾，所以return False.
                return False
            else:
                mem.add(n)
        else:
            return True