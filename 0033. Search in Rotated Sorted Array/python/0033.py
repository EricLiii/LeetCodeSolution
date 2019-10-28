class Solution_1:
"""
Link:https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

Idea:
1) Find middle point mid = (l + h)/2
2) If key is present at middle point, return mid.
3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..h]
4) Else (arr[mid+1..h] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[h], recur for arr[mid+1..h].
    b) Else recur for arr[l..mid] 

这个题主要就是理解只要arr[l] <= arr[mid]， 那么就是sorted的。自己可以写一点例子看看.

Runtime: 32 ms, faster than 91.71% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.2 MB, less than 62.96% of Python3 online submissions for Search in Rotated Sorted Array.
"""
    def search(self, nums: List[int], target: int) -> int:
        return self.customBinarySearch(nums, 0, len(nums)-1, target)
        
    def customBinarySearch (self, arr, l, h, key): 
        if l > h: 
            return -1

        mid = (l + h) // 2
        if arr[mid] == key: 
            return mid 

        # If arr[l...mid] is sorted  
        if arr[l] <= arr[mid]: #这里必须用<=判断，因为可能出现l==mid的情况.

            # As this subarray is sorted, we can quickly 
            # check if key lies in half or other half  
            if key >= arr[l] and key <= arr[mid]: 
                return self.customBinarySearch(arr, l, mid-1, key) 
            return self.customBinarySearch(arr, mid+1, h, key) 

        # If arr[l..mid] is not sorted, then arr[mid... r] 
        # must be sorted 
        if key >= arr[mid] and key <= arr[h]: 
            return self.customBinarySearch(arr, mid+1, h, key) 
        return self.customBinarySearch(arr, l, mid-1, key) 
        
class Solution_2:
"""
Runtime: 52 ms, faster than 51.07% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14 MB, less than 5.05% of Python3 online submissions for Search in Rotated Sorted Array.

Idea:
iterative solution.
"""
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid

            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1