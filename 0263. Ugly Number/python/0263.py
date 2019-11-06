class Solution_1:
"""
Runtime: 36 ms, faster than 84.53% of Python3 online submissions for Ugly Number.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Ugly Number.
"""
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1