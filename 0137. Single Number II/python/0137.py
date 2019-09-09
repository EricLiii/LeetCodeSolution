class Solution_1:
"""
Runtime: 72 ms, faster than 45.43% of Python3 online submissions for Single Number II.
Memory Usage: 15.8 MB, less than 6.67% of Python3 online submissions for Single Number II.

Link: https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

中文: http://liadbiz.github.io/leetcode-single-number-problems-summary/

没太明白，之后再看！
"""
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            b = (b ^ nums[i]) & ~a
            a = (a ^ nums[i]) & ~b
        return b
        
class Solution_1:
"""
和solution_1一样，但是更符合link中的解析.
"""
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        mask = 0
        for i in range(len(nums)):
            x2 ^= x1 & nums[i]
            x1 ^= nums[i]
            mask = ~ (x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1        
        
class Solution_2:
"""
Runtime: 68 ms, faster than 71.79% of Python3 online submissions for Single Number II.
Memory Usage: 15.7 MB, less than 6.67% of Python3 online submissions for Single Number II.

Link: https://www.jianshu.com/p/1da12a42a41d
"""
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while True:
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 3