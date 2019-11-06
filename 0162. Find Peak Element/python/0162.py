class Solution_1:
"""
Runtime: 52 ms, faster than 79.25% of Python3 online submissions for Find Peak Element.
Memory Usage: 13.9 MB, less than 5.48% of Python3 online submissions for Find Peak Element.

Idea:
Link:https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
 If an element(!!not the right-most one!!) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either 
   1. always increasing  -> the right-most element is the peak
   2. always decreasing  -> the left-most element is the peak
   3. first increasing then decreasing -> the pivot point is the peak
   4. first decreasing then increasing -> the left-most element is the peak  

   Therefore, we can find the peak only on its right elements(cut the array to half)

   The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.
   
   
   题目中You may imagine that nums[-1] = nums[n] = -∞.的意思是最左端和最右端的元素均无限小.因此必然存在峰值.
"""
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            # 正因两端元素无限小，所以nums[mid] == nums[mid+1]时可以right=mid-1.
            # 其实当nums[mid] == nums[mid+1]时也可以left=mid+1，一样通过.
            else:
                right = mid-1

        return left if nums[left] >= nums[right] else right
     
class Solution_2:
"""
Runtime: 52 ms, faster than 79.25% of Python3 online submissions for Find Peak Element.
Memory Usage: 13.9 MB, less than 5.48% of Python3 online submissions for Find Peak Element.

Idea:
Same idea with solution_1, but implement recursively.
"""
    def findPeakElement(self, nums: List[int]) -> int:
        return self.find(nums, 0, len(nums)-1)
        
    def find(self, nums, l, r):
        if l == r:
            return l
        if l == r-1:
            if nums[l] > nums[r]:
                return l
            else:
                return r
        mid = (l + r)//2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        if nums[mid] < nums[mid+1]:
            l = mid+1
            return self.find(nums, l, r)
        else:
            r = mid-1
            return self.find(nums, l, r)     
