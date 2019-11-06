class Solution_1:
"""
Author: Zefeng

Runtime: 48 ms, faster than 72.16% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

Idea:
Recursive solution.
"""
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        l, mid, r = 0, len(nums)//2, len(nums)-1
        if nums[0] < nums[mid]:
            minn = nums[0]
            #这里必须要判断minn和self.findMin(nums[mid+1:]谁更小.
            #因为当input是[3,1,2]的时候,如果直接返回self.findMin(nums[mid+1:]),结果是3而不是1.
            return min(minn, self.findMin(nums[mid+1:]))
        else:
            minn = nums[mid+1]
            #此处同理.
            return min(minn, self.findMin(nums[:mid+1]))
            
class Solution_2:
"""
Runtime: 52 ms, faster than 31.76% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

Idea;
Iterative solution.
"""
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) // 2
            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid
        return nums[start]