class Solution:
"""
Runtime: 200 ms, faster than 5.43% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 38.8 MB, less than 6.00% of Python3 online submissions for Product of Array Except Self.

https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space
"""
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [1 for _ in range(n)]
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
            
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
