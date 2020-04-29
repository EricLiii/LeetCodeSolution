class Solution_1:
"""
Runtime: 32 ms, faster than 93.93% of Python3 online submissions for Is Subsequence.
Memory Usage: 18.4 MB, less than 26.67% of Python3 online submissions for Is Subsequence.

https://leetcode.com/problems/is-subsequence/discuss/87258/2-lines-Python
"""
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
        
class Solution_2:
"""
Runtime: 276 ms, faster than 28.96% of Python3 online submissions for Is Subsequence.
Memory Usage: 18.1 MB, less than 26.67% of Python3 online submissions for Is Subsequence.

https://leetcode.com/problems/is-subsequence/discuss/87421/Python-simple-solution
"""
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s) 