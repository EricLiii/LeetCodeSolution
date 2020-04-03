class Solution:
"""
Runtime: 20 ms, faster than 99.07% of Python3 online submissions for Integer Break.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer Break.

Idea: https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem.
Code: https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
"""
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        product = 1
        while n>4:
            product *= 3
            n -= 3
        product *= n
        return product
