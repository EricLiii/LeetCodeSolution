class Solution_1:
"""
Author: Zefeng

Runtime: 52 ms, faster than 35.55% of Python3 online submissions for Permutations.
Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Permutations.
"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return self.helper(nums)
        
    def helper(self, lst):
        if not lst:
            return [[]]
        if len(lst) == 1:
            return [[lst[0]]]
        res = []
        for i in range(len(lst)):
            tmp = lst.pop(i)
            for item in self.helper(lst):
                res.append([tmp]+item)
            lst.insert(i, tmp)
        return res
        
class Solution_2:
"""
Runtime: 48 ms, faster than 71.61% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.

更简洁。
"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            #这里path+[nums[i]]其实是会创建一个新的list,所以不会影响path.
            #而res是传引用.
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)