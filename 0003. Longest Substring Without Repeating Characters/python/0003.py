class Solution:
"""
Runtime: 56 ms, faster than 92.62% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.9 MB, less than 5.05% of Python3 online submissions for Longest Substring Without Repeating Characters.

Idea:
Link: https://www.cnblogs.com/ariel-dreamland/p/8668286.html
"""
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        start = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            used[s[i]] = i
        return maxlen