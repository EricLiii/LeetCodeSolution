class Solution:
"""
Author: Zefeng

Runtime: 176 ms, faster than 12.35% of Python3 online submissions for Combination Sum.
Memory Usage: 13.3 MB, less than 31.77% of Python3 online submissions for Combination Sum.

Idea: Depth-first search.
"""
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                    dfs(nums, target-nums[i], pre + [nums[i]], res)
        pre = []
        res = []
        candidates.sort()
        dfs(candidates, target, pre, res)
        return res
        

    def wrongCode_combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, pre, res):
            for i in range(len(nums)):
                if nums[i] > target:
                    pre = []   #这里不应该清零pre
                    return
                elif nums[i] == target:
                    temp = pre + [nums[i]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    pre = []    #这里不应该清零pre
                    return
                else:
                    pre = pre + [nums[i]]   #这里不应该改变pre的值，而是应该以(pre+[nums[i]])的形式赋给下一个迭代。
                    dfs(nums, target-nums[i], pre, res)
        pre = []
        res = []
        candidates.sort()
        dfs(candidates, target, pre, res)
        return res
        
class Solution:
"""
Author: Zefeng

Runtime: 60 ms, faster than 91.60% of Python3 online submissions for Combination Sum.
Memory Usage: 13.1 MB, less than 85.46% of Python3 online submissions for Combination Sum.

Improved code based on the solution above
"""
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, pre, res):
            for i in range(len(nums)):
                if nums[i] > target:
                    return
                elif nums[i] == target:
                    temp = pre + [nums[i]]
                    #temp.sort()不需要再次sort了，因为candidates已经sort了.
                    if temp not in res:
                        res.append(temp)
                    return
                else:
                    #改进点在这里，每次迭代不要将nums全部输入，而是只从第i项开始输入。这是为了避免重复寻找相同的解。
                    #比如，nums = [3，4，7，8]，target = 11：
                    #    [3,8]是以3为起始点时找到的解，[8,3]是以8为起始点找到的解。这两个解重复了。其实在以8为起始点时，不必再从8前面的项中找，
                    #    因为找出的包括前面项的解一定在前面的寻找中已经找到了。这样就大大减少了运行时间。
                    #从i开始是为了允许重复使用自身。
                    dfs(nums[i:], target-nums[i], pre + [nums[i]], res)
        pre = []
        res = []
        candidates.sort()
        dfs(candidates, target, pre, res)
        return res
    

class Solution:    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return 
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            #他这里用index来防止重复寻找解，跟我的代入num[i]其实是一致的。
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
        
