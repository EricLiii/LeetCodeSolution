class Solution:
    """
    Runtime: 5232 ms, faster than 22.55% of Python3 online submissions for Two Sum.
    Memory Usage: 13.8 MB, less than 74.29% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    
class Solution:
    """
    Runtime: 32 ms, faster than 97.00% of Python3 online submissions for Two Sum.
    Memory Usage: 14.5 MB, less than 28.00% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target-v], i]
            d[v] = i
