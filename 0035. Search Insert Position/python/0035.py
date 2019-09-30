class Solution:
"""
Runtime: 32 ms, faster than 90.83% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.6 MB, less than 85.00% of Python3 online submissions for Search Insert Position.

Binary search
"""
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 72.27% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.4 MB, less than 98.74% of Python3 online submissions for Search Insert Position.
"""
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)     