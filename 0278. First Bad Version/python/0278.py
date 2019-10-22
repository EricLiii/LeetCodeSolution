class Solution_1:
"""
Runtime: 32 ms, faster than 88.91% of Python3 online submissions for First Bad Version.
Memory Usage: 13.9 MB, less than 6.90% of Python3 online submissions for First Bad Version.

https://leetcode.com/problems/first-bad-version/discuss/71324/Python-understand-(easily-from-Binary-search-idea)

这个题容易错的，要自己再做一遍.


TODO: 当n=2, first_bad=2, 根据code输出是1, 但是网站上给出的结果是2. 那为什么这个code可以通过???
"""
    def firstBadVersion(self, n):
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left #return left 和 return right区别很大.