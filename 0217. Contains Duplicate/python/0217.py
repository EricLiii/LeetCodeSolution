class Solution:
"""
Author: Zefeng

Runtime: 144 ms, faster than 63.64% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19 MB, less than 24.53% of Python3 online submissions for Contains Duplicate.
"""
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        
class Solution:
"""
Runtime: 136 ms, faster than 93.86% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.4 MB, less than 15.09% of Python3 online submissions for Contains Duplicate.
"""
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums) == len(set(nums)))