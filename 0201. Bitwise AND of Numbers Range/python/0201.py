class Solution_1:
"""
Runtime: 68 ms, faster than 69.31% of Python3 online submissions for Bitwise AND of Numbers Range.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.

https://www.cnblogs.com/grandyang/p/4431646.html

https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation
"""
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i