
"Link: https://leetcode.com/problems/power-of-two/discuss/63966/4-different-ways-to-solve-Iterative-Recursive-Bit-operation-Math"

class Solution_1:
"""
Runtime: 36 ms, faster than 83.80% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Power of Two.
"""
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False
        while n % 2 == 0: 
            n /= 2
        return n == 1
        
class Solution_2:
"""
Runtime: 40 ms, faster than 57.85% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Power of Two.

位操作。
"""
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n-1)