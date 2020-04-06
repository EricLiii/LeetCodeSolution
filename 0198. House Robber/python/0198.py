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
        # 这里len(nums)+2是为了避免判断nums的长度，后面用nums[i-2],一步到位.更简洁!!!
        for i in range(2, len(nums)+2):
            pre, prep = max(pre, prep + nums[i-2]), pre
        return pre
        
class Solution_3:
"""
Runtime: 36 ms, faster than 81.62% of Python3 online submissions for House Robber.
Memory Usage: 13.6 MB, less than 9.09% of Python3 online submissions for House Robber.


"""
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        prev, pre = nums[0], max(nums[0], nums[1])
        #这里因为判断了nums的长度,所以后面可以直接用nums[i].
        for i in range(2, len(nums)):
            prev, pre = pre, max(pre, nums[i]+prev)
        return pre
        
class Solution_4:
"""
Zefeng

House Robber.
Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.

记这个，最简洁!
"""
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p1, p2 = 0, nums[0]
        for i in range(1, len(nums)):
            p1, p1 = p2, max(p1+nums[i], p1)        
        return p2