class Solution_1:
"""
Author: Zefeng

Runtime: 36 ms, faster than 79.82% of Python3 online submissions for House Robber.
Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.

Idea:
DP.
"""
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        return max(dp)
        
class Solution_2:
"""
Runtime: 36 ms, faster than 79.82% of Python3 online submissions for House Robber.
Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.

其实不需要建立一个列表，只需要有两个值就行。
"""
    def rob(self, nums: List[int]) -> int:
        prep, pre = 0, 0
        for i in range(2, len(nums)+2):
            pre, prep = max(pre, prep + nums[i-2]), pre
        return pre