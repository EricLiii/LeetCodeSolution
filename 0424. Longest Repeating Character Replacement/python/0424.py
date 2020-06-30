class Solution:
"""
Runtime: 108 ms, faster than 87.02% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 13.9 MB, less than 39.23% of Python3 online submissions for Longest Repeating Character Replacement.

https://leetcode.com/problems/longest-repeating-character-replacement/submissions/

好好看，很巧妙
"""
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res