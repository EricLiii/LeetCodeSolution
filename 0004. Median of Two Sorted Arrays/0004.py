class Solution:
"""
Runtime: 104 ms, faster than 88.48% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

https://blog.csdn.net/qq_28466517/article/details/79810809
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
"""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        # 因为计算i的时候是i = (imin + imax) // 2， 向下取整，所以要判断imin <= imax, 而不是imin < imax.
        # 不然有些值取不到.
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                # 这里判断i,j 是否为0是为了防止i-1,j-1超出范围.
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left
                   
                # 同理，这里也是为了防止超出范围.
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0