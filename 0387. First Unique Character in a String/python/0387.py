class Solution:
"""
Runtime: 96 ms, faster than 77.11% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.

https://leetcode.com/problems/first-unique-character-in-a-string/discuss/169270/Simple-Python
"""
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1