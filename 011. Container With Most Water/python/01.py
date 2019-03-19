class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=(right-left)*min(height[left],height[right])
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            max_area=max(max_area, (right-left)*min(height[left],height[right]))
        return max_area
