class Solution_1:
"""
Runtime: 100 ms, faster than 54.64% of Python3 online submissions for Basic Calculator II.
Memory Usage: 15.4 MB, less than 11.11% of Python3 online submissions for Basic Calculator II.

https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
"""
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)