class Solution_1:
"""
Runtime: 44 ms, faster than 17.27% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 5.47% of Python3 online submissions for Merge Sorted Array.
"""
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        if i<0:
            nums1[:k+1]=nums2[:j+1]
            
class Solution_2:
"""
Runtime: 40 ms, faster than 56.92% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 5.47% of Python3 online submissions for Merge Sorted Array.

Idea: 
Same idea with solution_1, but more concise.

这道题主要就是要明白存在 nums1 = [0], m = 0; nums2 = [1], n = 1 这个edge case.
"""
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                #从后往前放，这样不会污染nums1原来的值.
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0: #handle edge case.
            nums1[:n] = nums2[:n]
