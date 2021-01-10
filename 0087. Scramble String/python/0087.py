class Solution_1:
"""
Runtime: 48 ms, faster than 54.62% of Python3 online submissions for Scramble String.
Memory Usage: 14.3 MB, less than 62.04% of Python3 online submissions for Scramble String.


https://leetcode.com/problems/scramble-string/discuss/29459/Python-recursive-solution
思路比较简单，就是容易超时。
"""
    def isScramble(self, s1: str, s2: str) -> bool:
        # 进行一些判断从而避免超时
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True
        
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[::-1][:i]) and self.isScramble(s1[i:], s2[::-1][i:])):
                return True

        return False