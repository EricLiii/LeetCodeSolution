class Solution_1:
"""
Runtime: 20 ms, faster than 57.10% of Python online submissions for Reverse Bits.
Memory Usage: 11.7 MB, less than 57.14% of Python online submissions for Reverse Bits.
"""
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res
        
class Solution_2:
"""
Runtime: 16 ms, faster than 81.87% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 39.29% of Python online submissions for Reverse Bits.
"""
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #注意： 二进制前两个字符是'0b',所以要从第三个字符开始.
        return int(bin(n)[2:].zfill(32)[::-1], 2)