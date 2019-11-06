class Solution:
    """
    Runtime: 68 ms, faster than 47.40% of Python3 online submissions for Container With Most Water.
    Memory Usage: 14.7 MB, less than 7.66% of Python3 online submissions for Container With Most Water.
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = (right-left) * min(height[left],height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, (right-left)*min(height[left],height[right]))
        return max_area
