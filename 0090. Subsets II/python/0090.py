class Solution_1:
"""
Runtime: 52 ms, faster than 32.02% of Python3 online submissions for Subsets II.
Memory Usage: 13.9 MB, less than 5.58% of Python3 online submissions for Subsets II.
"""
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        path.sort() # sort() is an in-place operation.
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
class Solution_2:
"""
Runtime: 44 ms, faster than 86.06% of Python3 online submissions for Subsets II.
Memory Usage: 13.9 MB, less than 5.58% of Python3 online submissions for Subsets II.

Idea:
if nums[i] is same to nums[i-1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding nums[i-1].
For example: 
 Input[1,2,2]
    itemOfNums      cur               res
                    []                [[]]
    ---------------------------------------
        [1]         [[1]]             [[],[1]]
    ---------------------------------------
        [2]         [[2],[1,2]]       [[],[1],[2],[1,2]]
    ----------------------------------------------------
        [2]         [[2,2],[1,2,2]]   [[],[1],[2],[1,2],[2,2],[1,2,2]]
                               
"""
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res