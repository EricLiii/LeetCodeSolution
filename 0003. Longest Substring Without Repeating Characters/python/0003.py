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
        used = {} #当时没想到用一个dict来保存字母出现的位置.
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            used[s[i]] = i #记得要更新字母最近出现的位置.
        return maxlen
        
class Solution:
"""
Runtime: 64 ms, faster than 72.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 18.30% of Python3 online submissions for Longest Substring Without Repeating Characters.

Zefeng
和solution_1一样
"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        max_len = 0
        cur_len = 0
        start = 0
        
        for i, c in enumerate(s):
            if c not in visited:
                visited[c] = i
                cur_len += 1
            else:
                if start > visited[c]:
                    visited[c] = i
                    cur_len += 1
                else:
                    start = visited[c] + 1
                    cur_len = i - visited[c]
                    visited[c] = i
            max_len = max(max_len, cur_len)
        return max_len