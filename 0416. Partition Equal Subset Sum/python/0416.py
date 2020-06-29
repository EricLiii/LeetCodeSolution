class Solution:
"""
Runtime: 792 ms, faster than 53.12% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 13.8 MB, less than 93.32% of Python3 online submissions for Partition Equal Subset Sum.

https://www.cnblogs.com/grandyang/p/5951422.html
DP
"""
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        half = int(sum(nums)/2)

        dp = [False] * (half+1)
        dp[0] = True
        
        for i in range(len(nums)):
            #最重要的就是这里要倒序遍历!正序的话就全是true了.
            for j in range(half, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
                
        return dp[-1]