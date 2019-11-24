class Solution:
"""
Runtime: 124 ms, faster than 92.00% of Python3 online submissions for Edit Distance.
Memory Usage: 15 MB, less than 92.31% of Python3 online submissions for Edit Distance.

https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

https://www.cnblogs.com/grandyang/p/4344107.html
"""
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.helper(word1, word2, 0, 0, memo)
          
    def helper(self, word1, word2, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.helper(word1, word2, i + 1, j + 1, memo)
            else: 
                insert = 1 + self.helper(word1, word2, i, j + 1, memo)
                delete = 1 + self.helper(word1, word2, i + 1, j, memo)
                replace = 1 + self.helper(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]