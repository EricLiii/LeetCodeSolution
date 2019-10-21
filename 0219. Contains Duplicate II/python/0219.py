class Solution:
"""
Runtime: 108 ms, faster than 71.58% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 21.5 MB, less than 37.50% of Python3 online submissions for Contains Duplicate II.
"""
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False