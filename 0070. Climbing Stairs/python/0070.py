class Solution_1:
"""
这个方法多考虑了edge case，没必要。
记solution_2。
"""
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return 0
        if n<=2:
            return n
        stairs,prev=2,1
        for _ in range(3,n+1):
            stairs,prev=stairs+prev,stairs
        return stairs

class Solution_2:
"""
Author: Zefeng

Runtime: 36 ms, faster than 66.12% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
"""
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        prep, pre = 0, 1
        for i in range(n):
            prep, pre = pre, prep+pre
        return pre
        
class Solution_3:
"""
可以用递归，但是超时。
"""
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)