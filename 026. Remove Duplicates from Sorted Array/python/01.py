class Solution_1:
"""
Runtime: 60 ms, faster than 68.77% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 55.53% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
    def removeDuplicates(self, nums: List[int]) -> int:
        next_new=0
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nums[next_new]=nums[i] #insert the element at the beginning of the list, doesn't create new array.
                next_new+=1
        return next_new
        
class Solution_2:
"""
Author: Zefeng

Runtime: 88 ms, faster than 12.55% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 42.85% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        index = 0
        while index < len(nums) and count < len(nums):
            if index > 0 and nums[index] == nums[index-1]:
                nums.append(nums.pop(index))
            else:
                index += 1
            count += 1
        return len(nums[:index])
