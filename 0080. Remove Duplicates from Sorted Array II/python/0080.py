class Solution_1:
"""
Author: Zefeng

Runtime: 72 ms, faster than 10.93% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.9 MB, less than 5.46% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3:
            return l
        count = 0
        cur = 2
        while count < l - 2: #这里注意，因为已经排除了nums长度小于3的情况，这里count不再需要小于l.
            if nums[cur] == nums[cur-1] == nums[cur-2]:
                nums.pop(cur)
            else:
                cur += 1
            count += 1
        return cur
        
class Solution_2:
"""
Runtime: 64 ms, faster than 10.93% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.9 MB, less than 5.46% of Python3 online submissions for Remove Duplicates from Sorted Array II.

Idea:
用一个探针记录位置，代码更短。
"""
    def removeDuplicates(self, nums: List[int]) -> int:
        probe = 0
        for n in nums:
            if probe < 2 or n > nums[probe-2]:
                nums[probe] = n
                probe += 1
        return probe