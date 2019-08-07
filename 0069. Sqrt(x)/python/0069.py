class Solution_1:
"""
Runtime: 44 ms, faster than 62.75% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for Sqrt(x).

牛顿法。
"""
    def mySqrt(self, x: int) -> int:
        if (x==0):
            return 0
        guess=x/2
        goon=True
        while goon:
            avg=(guess+x/guess)/2
            if (avg//1==guess//1):
                goon=False
            else:
                guess=avg
        return int(guess//1)
        
class Solution_2:
"""
Runtime: 40 ms, faster than 81.89% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.7 MB, less than 5.56% of Python3 online submissions for Sqrt(x).

Idea:
牛顿法更简单的实现。
需要注意的是，牛顿迭代法不一定总是收敛的，但是对于求平方根这个问题，总是收敛的。

牛顿法的推导要会： https://blog.csdn.net/ccnt_2012/article/details/81837154
具体见summary->LeetCode.docx:0069.
"""
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r
        
class Solution_3:
"""
Runtime: 40 ms, faster than 81.89% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.1 MB, less than 5.56% of Python3 online submissions for Sqrt(x).

Idea:
Binary search.
"""
    def mySqrt(self, x: int) -> int:
        """如果初始化left, right = 1, x, 需要handle以下edge case
        if x == 0:
            return 0
        """
        left, right = 0, x
        # left < right 或者 left < right对结果没有影响。
        while left <= right:
            #也可用mid = (left+right)//2
            mid = left + (right-left)//2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid < x:
                #为了保证input=1的情况。
                #如果一开始有if x == 1: return 1的语句，则left = mid即可。
                left = mid + 1  
            else:
                right = mid
        return left
