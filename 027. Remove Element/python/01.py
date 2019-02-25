class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[next]=nums[i]
                next+=1
        return next
