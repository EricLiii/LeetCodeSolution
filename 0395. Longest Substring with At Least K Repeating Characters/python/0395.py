class Solution_1:
"""
Runtime: 36 ms, faster than 49.05% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python

"""
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c)) #split是精髓.
        return len(s)