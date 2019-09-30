class Solution:
"""
Runtime: 116 ms, faster than 64.64% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.2 MB, less than 33.86% of Python3 online submissions for 3Sum Closest.
"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return result     


class Solution:
"""
Author: Zefeng

Runtime: 132 ms, faster than 43.12% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.3 MB, less than 10.53% of Python3 online submissions for 3Sum Closest.
"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            return None
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] +nums[r]
                if s - target == 0:
                    return s
                else:
                    if abs(s - target) < abs(res - target):
                        res = s
                    if s - target > 0:
                        r -=1
                    else:
                        l += 1
        return res        
                    
