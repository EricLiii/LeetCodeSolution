class Solution:
    def reverse(self, x: int) -> int:
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x //= 10
        return res * isPos
        
#Runtime: 68 ms, faster than 41.81% of Python3 online submissions for Reverse Integer.
#Memory Usage: 13.4 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
