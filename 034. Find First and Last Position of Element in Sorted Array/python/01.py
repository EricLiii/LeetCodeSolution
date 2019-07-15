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