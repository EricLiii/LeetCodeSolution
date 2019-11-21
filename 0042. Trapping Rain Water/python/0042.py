class Solution:
"""
Runtime: 48 ms, faster than 97.35% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.5 MB, less than 81.40% of Python3 online submissions for Trapping Rain Water.

https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
""'
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        maxleft, maxright = 0, 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] >= maxleft:
                    maxleft = height[l]
                else:
                    res += maxleft - height[l]
                l += 1
            else:
                if height[r] >= maxright:
                    maxright = height[r]
                else:
                    res += maxright - height[r]
                r -= 1
        return res
