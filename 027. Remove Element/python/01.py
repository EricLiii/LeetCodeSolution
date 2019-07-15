class Solution:
"""
Runtime: 32 ms, faster than 93.76% of Python3 online submissions for Remove Element.
Memory Usage: 13.2 MB, less than 36.04% of Python3 online submissions for Remove Element.
"""
    def removeElement(self, nums: List[int], val: int) -> int:
        next=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[next]=nums[i]
                next+=1
        return next

        
class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 77.60% of Python3 online submissions for Remove Element.
Memory Usage: 13.2 MB, less than 38.96% of Python3 online submissions for Remove Element.
"""
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        count = 0
        while index < len(nums) and count < len(nums):
            if nums[index] == val:
                nums.append(nums.pop(index))
            else:
                index += 1
            count += 1
        return len(nums[:index])