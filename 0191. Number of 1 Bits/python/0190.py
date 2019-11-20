class Solution(object):
"""
Runtime: 20 ms, faster than 49.84% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 57.50% of Python online submissions for Number of 1 Bits.
"""
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:  #直接while n: 也可以，好像更快。
            if n & 1:
                count += 1
            n >>= 1
        return count
        
class Solution(object):
"""
Runtime: 16 ms, faster than 78.03% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 32.50% of Python online submissions for Number of 1 Bits.

使用了内置函数.
"""
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')