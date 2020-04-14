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

https://blog.csdn.net/wilzxu/article/details/88655366
那么这个dp到底在维护什么？可以这样理解：dp[i]维护的是长度为i+1的递增子序列可以取到的最小结尾值。
当替换前面的元素时，会将一个位置上的值尽可能缩小，虽然替换可能破坏了原有的LIS，但是却保留了获得更长LIS的可能性。
比如说上面的例子，遍历到8的时候我们以为长度为2的序列必须以8结尾，但是到4的时候我们就可以选择以4结尾。
而之后能够获得的LIS如果可以和[0, 8]续接那么一定可以和[0,4]续接。
2最后替换了4是因为如果后面还有数字，可能以同样的原理接在[0,2]后面。
为什么长度一定是LIS的正确长度呢？因为每次增加dp长度的条件是nums[i]大于之前所有数，
这个新的LIS是真实存在的，不管之后会不会被替换。多试几个栗子体会。


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
