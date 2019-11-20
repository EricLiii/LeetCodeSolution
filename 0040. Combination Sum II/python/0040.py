class Solution_1:
"""
Author: Zefeng

Runtime: 68 ms, faster than 60.94% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.3 MB, less than 43.12% of Python3 online submissions for Combination Sum II.
"""
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, pre, res):
            for i in range(len(nums)):
                if nums[i] > target:
                    return
                elif nums[i] == target:
                    temp = pre + [nums[i]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    return
                else:
                    #相比于combination sum，只是从第i+1项开始输入即可。
                    dfs(nums[i+1:], target-nums[i], pre + [nums[i]], res)
        pre = []
        res = []
        candidates.sort()
        dfs(candidates, target, pre, res)
        return res

class Solution_2:
"""
Runtime: 44 ms, faster than 96.58% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.4 MB, less than 21.26% of Python3 online submissions for Combination Sum II.
"""
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, index, path, res):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > target:
                    break
                dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res
        
class Solution_3:
"""
Author: Zefeng

Runtime: 48 ms, faster than 90.39% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.2 MB, less than 56.38% of Python3 online submissions for Combination Sum II.

Improved my code based on solution_2：
solution_1比solution_2慢的原因是，当input包含重复数字时（例[10,1,2,7,6,1,5]），solution_1在两次以1为起始点时都会进行计算。
其实在第二次以1为起始点时可以跳过。
"""
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, pre, res):
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    return
                elif nums[i] == target:
                    res.append(pre + [nums[i]])
                    return
                else:
                    dfs(nums[i+1:], target-nums[i], pre + [nums[i]], res)
        pre = []
        res = []
        candidates.sort()
        dfs(candidates, target, pre, res)
        return res