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