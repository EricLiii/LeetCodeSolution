class Solution:
"""
Runtime: 104 ms, faster than 98.09% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Largest Rectangle in Histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

https://www.cnblogs.com/grandyang/p/4322653.html
"""
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # 注意这里的stack[-1]跟前面的已经不一样了，以为经历了stack.pop()
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans