class Solution_1:
"""
Runtime: 1040 ms, faster than 5.10% of Python3 online submissions for Permutations II.
Memory Usage: 14 MB, less than 8.89% of Python3 online submissions for Permutations II.

一个很烂的方法就是在0046基础上加个判断，很慢很慢!
"""
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            if path not in res:
                res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
class Solution_2:
"""
Runtime: 60 ms, faster than 89.72% of Python3 online submissions for Permutations II.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Permutations II.

solution_1加判断的方式不好，记solution_2.
"""
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        #要先排序
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            #加判断
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)