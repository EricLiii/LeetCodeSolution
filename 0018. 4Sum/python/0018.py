class Solution_1:
"""
Runtime: 88 ms, faster than 92.16% of Python3 online submissions for 4Sum.
Memory Usage: 13.3 MB, less than 49.80% of Python3 online submissions for 4Sum.
"""
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
               # careful about range, 但是range(len(nums))也是可以通过的。
            for i in range(0, len(nums)-N+1):   
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return

class Solution_2:
"""
Author: Zefeng

Runtime: 216 ms, faster than 61.22% of Python3 online submissions for 4Sum.
Memory Usage: 13.1 MB, less than 90.78% of Python3 online submissions for 4Sum.
"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = self.nSum(4, nums, target)
        return res
        
    def nSum(self, N, nums, target):
        nums.sort()
        res = []  #相比solution_1，只开辟一块空间，降低了空间复杂度。
        if N < 2:
            return nums
        elif N == 2:
            lst = []
            for i in range(len(nums)):          #这个方法就没有solution_1的快，因为solution_1是从两边往中间走，而这里是从开头遍历。
                if target - nums[i] in lst:
                    if [target - nums[i], nums[i]] not in res:
                        res.append([target - nums[i], nums[i]])
                lst.append(nums[i])
            return res
        else:
            for i in range(len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N: #这一行很有必要，时间从2068ms直接降到216ms。
                    break
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                lst = self.nSum(N-1, nums[i+1:], target - nums[i])
                for item in lst:  #这里比solution_1多加了一个for循环，于是O(n)变成了O(n^2)
                    if item:
                        item.insert(0, nums[i])
                        if item not in res:
                            res.append(item)
            return res
        
        
class Solution_3:
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
        
        
class Solution_4:
"""
Runtime: 116 ms, faster than 81.63% of Python3 online submissions for 4Sum.
Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for 4Sum.
"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.nSum(nums, target, [], 4)
        return self.res
        
    def nSum(self, nums, target, path, n):
        if n < 2:
            return
        elif n == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    self.res.append(path + [nums[l]] + [nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        elif n > 2:
            for i in range(len(nums)):
                if target < nums[i]*n or target > nums[-1]*n: #必不可少的.
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target - nums[i], path + [nums[i]], n - 1)
        return
