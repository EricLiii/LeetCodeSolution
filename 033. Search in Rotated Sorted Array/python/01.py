class Solution:
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
        if arr[l] <= arr[mid]: 

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