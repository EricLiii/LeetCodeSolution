class Solution:
"""
Runtime: 100 ms, faster than 92.52% of Python3 online submissions for Jump Game II.
Memory Usage: 14.8 MB, less than 8.33% of Python3 online submissions for Jump Game II.

https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
"""
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
