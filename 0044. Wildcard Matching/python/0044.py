class Solution:
"""
Runtime: 908 ms, faster than 38.48% of Python3 online submissions for Wildcard Matching.
Memory Usage: 22.4 MB, less than 60.54% of Python3 online submissions for Wildcard Matching.

https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
"""
    def isMatch(self, s: str, p: str) -> bool:
        M = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        
        M[0][0] = True
        
        # s is empty, find continuous "*" in p
        for j in range(1, len(p)+1):
            if p[j-1] != "*":
                break
            else:
                M[0][j] = True
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == "?":
                    M[i][j] = M[i-1][j-1]
                elif p[j-1] == "*":
                    M[i][j] = M[i-1][j-1] or M[i-1][j] or M[i][j-1]

        return M[-1][-1]