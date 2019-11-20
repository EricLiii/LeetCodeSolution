class Solution_1:
"""
Author: Zefeng

Runtime: 952 ms, faster than 56.10% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.
"""
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            tmp = [1]
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp.append(dp[j]+1)
            dp.append(max(tmp))
        return max(dp) 


class Solution_2:
"""
Runtime: 36 ms, faster than 99.68% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.

https://www.cnblogs.com/grandyang/p/4938187.html
https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

So the main idea is:
Use binary search to either
-- extend increasing sequence with larger numbers, or
-- minimize existing values with smaller ones - so we can use smaller numbers to extend it.
"""
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ends = [nums[0]]
        for n in nums:
            if n < ends[0]:
                ends[0] = n
            elif n > ends[-1]:
                ends.append(n)
            else:
                l, r = 0, len(ends)-1
                while l < r:
                    mid = (l + r) // 2
                    if ends[mid] < n:
                        l = mid + 1
                    else:
                        r = mid
                ends[r] = n
        return len(ends)
