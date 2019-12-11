class Solution:
"""
Link: https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

Runtime: 36 ms, faster than 84.81% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 13.9 MB, less than 28.31% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

There are better solutions in discussion, but not easy to understand. Study later.
"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums, 0, len(nums)-1, target, len(nums)), self.last(nums, 0, len(nums)-1, target, len(nums))]
    
    def first(self, arr, low, high, x, n) : 
        if(high >= low) : 
            mid = low + (high - low) // 2
            if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
                return mid 
            elif(x > arr[mid]) : 
                return self.first(arr, (mid + 1), high, x, n) 
            else : 
                return self.first(arr, low, (mid - 1), x, n) 
        return -1

    def last(self, arr, low, high, x, n) : 
        if (high >= low) : 
            mid = low + (high - low) // 2
            if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
                return mid 
            elif (x < arr[mid]) : 
                return self.last(arr, low, (mid - 1), x, n) 
            else : 
                return self.last(arr, (mid + 1), high, x, n) 
        return -1
        
        
class Solution:
"""
Runtime: 100 ms, faster than 76.76% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.9 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

这道题主要是得想到用两个bs,一个是解决不了的。
"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1 # +1是重点！！
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]


class Solution:
"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14714/16-line-Python-solution-symmetric-and-clean-binary-search-52ms

记这个不错
"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right: #这里是<=
                mid = (left + right) // 2
                if x > A[mid]: #这里是>
                    left = mid + 1
                else: 
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right: #这里是<=
                mid = (left + right) // 2
                if x >= A[mid]: #这里是>=
                    left = mid + 1
                else: 
                    right = mid - 1
            return right
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
