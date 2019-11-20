class Solution:
"""
Runtime: 44 ms, faster than 92.95% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Valid Parentheses.

https://leetcode.com/problems/longest-valid-parentheses/discuss/123926/Best-Python-Solution-(Beats-100)
"""
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest