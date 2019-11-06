class Solution_1:
"""
Runtime: 160 ms, faster than 50.55% of Python3 online submissions for Missing Number.
Memory Usage: 15.1 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))
        
class Solution_2:
"""
Runtime: 160 ms, faster than 50.55% of Python3 online submissions for Missing Number.
Memory Usage: 15.8 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1)) - set(nums)).pop()
        

class Solution_3:
"""
Runtime: 164 ms, faster than 36.74% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 6.45% of Python3 online submissions for Missing Number.

https://www.cnblogs.com/yrbbest/p/5022828.html
https://leetcode.com/problems/missing-number/discuss/69791/4-Line-Simple-Java-Bit-Manipulate-Solution-with-Explaination

位操作!!
"""
    def missingNumber(self, nums: List[int]) -> int:
        xor, a = 0, 0
        for i in range(len(nums)):
            xor = xor ^ a ^ nums[i]
            a += 1
        return xor ^ a