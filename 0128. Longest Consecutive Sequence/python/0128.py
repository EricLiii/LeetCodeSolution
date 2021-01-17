class Solution_1:
"""
Runtime: 52 ms, faster than 84.58% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 15.2 MB, less than 70.37% of Python3 online submissions for Longest Consecutive Sequence.

Zefeng

思路就是找到nums中的最大值和最小值，以这个长度建立一个列表，让后往里面放元素。
然后再遍历一遍看最长的连续的子列有多长。
"""
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxx = max(nums)
        minn = min(nums)
        # minn, maxx都有可能大于，小于或等于0.
        # 当index<0的时候列表的访问方式会与我们的想法冲突
        # 所以用一个offset来将nums中最小的int移动到index 0位置。
        offset = 0 - minn
        
        lst = [-1] * (maxx - minn + 1)
        for n in nums:
            lst[n + offset] = 1
        
        res = 0
        tmp = 0
        for i in range(len(lst)):
            if lst[i] != -1:
                tmp += 1
                res = max(res, tmp)
            else:
                res = max(res, tmp)
                tmp = 0
        return res

        
class Solution_2:
"""
Runtime: 56 ms, faster than 65.71% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 15.4 MB, less than 51.80% of Python3 online submissions for Longest Consecutive Sequence.

https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
"""
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            # 这一行让这个算法变为O(N). 有才.
            # 自己写一下input为[1,2,3,4,5]时候的情况就明白了。
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best