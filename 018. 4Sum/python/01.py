class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
        
class Solution:
"""
Author: Zefeng

Runtime: 944 ms, faster than 39.60% of Python3 online submissions for 4Sum.
Memory Usage: 13.3 MB, less than 49.77% of Python3 online submissions for 4Sum.
"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                #必须有i>0，否则若i=0，i-1=-1会取list末尾的值;
                #第i项和第i-1项比较，而不是第i项和第i+1项比较: 因为第i项可能会用到第i+1项，但是第i项的情况一定包含在第i-1项内(当第i项==第i-1项时).
                continue
            temp = self.threeSum(nums[i+1:], target-nums[i]) #注意从i+1开始取新list.
            for item in temp:
                if item:
                    item.append(nums[i])
                    item = sorted(item)
                    result.append(item)
        return result
        
    def threeSum(self, nums, target):
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res
