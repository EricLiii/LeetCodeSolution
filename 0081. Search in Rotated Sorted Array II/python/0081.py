class Solution_1:
"""
Runtime: 64 ms, faster than 62.92% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.1 MB, less than 5.49% of Python3 online submissions for Search in Rotated Sorted Array II.
"""
    def search(self, nums: List[int], target: int) -> bool:
        return self.customBinarySearch(nums, 0, len(nums)-1, target)
        
    def customBinarySearch (self, arr, l, h, key): 
        if l > h: 
            return False

        mid = (l + h) // 2
        if arr[mid] == key: 
            return True
            
        #Handle edge case
        #因为下面先比较l和mid，所以这里只需handle左边的情况，右边的可以不管。
        #如果下面先比较mid和h，这里就要 while mid < h and arr[mid]== arr[h],左边可以不管。
        #当然以为可以两边同时管，如solution_2.
        while l < mid and arr[l] == arr[mid]:
            l += 1
            
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
        
class Solution_2:
"""
Runtime: 64 ms, faster than 62.92% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.2 MB, less than 5.49% of Python3 online submissions for Search in Rotated Sorted Array II.

Idea:
Link:https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)

The only difference is that due to the existence of duplicates, 
we can have nums[left] == nums[mid] and in that case, 
the first half could be out of order (i.e. NOT in the ascending order, e.g. [3 1 2 3 3 3 3]) 
and we have to deal this case separately. In that case, it is guaranteed that nums[right] also equals to nums[mid], 
so what we can do is to check if nums[mid]== nums[left] == nums[right] before the original logic, 
and if so, we can move left and right both towards the middle by 1. and repeat.
"""
    def search(self, nums: List[int], target: int) -> bool:
        return self.customBinarySearch(nums, 0, len(nums)-1, target)
        
    def customBinarySearch (self, arr, l, h, key): 
        if l > h: 
            return False

        mid = (l + h) // 2
        if arr[mid] == key: 
            return True
        while l < mid and mid < h and arr[l] == arr[mid] == arr[h]:
            l += 1
            h -= 1
        """
        或者把上面的替换成这段.这个比较好记.
        其实所有检查的目的都是为了避免nums[l] == nums[mid]或者nums[mid] == nums[r]对是否是排序的检查的干扰.
        所以可以只查nums[l] == nums[mid]，也可以只查nums[mid] == nums[r]，还可以同时查arr[l] == arr[mid] == arr[h]。
        while l < mid and nums[l] == nums[mid]:
            l += 1
        while mid < r and nums[mid] == nums[r]:
            r -= 1
        """
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
        
class Solution_3:
"""
Runtime: 64 ms, faster than 62.92% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.1 MB, less than 5.49% of Python3 online submissions for Search in Rotated Sorted Array II.

Idea:
Iterative solution.
"""
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
                
            # tricky part
            #OR: while l < mid and mid < r and nums[l] == nums[mid] == nums[r]:
            #       l += 1
            #       r -= 1
            while l < mid and nums[l] == nums[mid]: 
                l += 1
                
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
        return False