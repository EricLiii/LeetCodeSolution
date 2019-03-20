class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return result       
                    
