class Solution_1:
"""
Runtime: 76 ms, faster than 82.35% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.1 MB, less than 8.70% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                #减法和除法需要注意操作顺序。
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                #当正数除以负数的时候，先做float除法，再转换为int型，可以让结果truncate to zero.
                #e.g., 1/-2 = -0.5, 1//-2 = -1, 这显然不是truncate to zero.
                #      而 int(1/-2) = 0, 符合要求.
                stack.append(int(stack.pop(-2)/stack.pop(-1)))
            else:
                #每个数字都在这里进行int转换了,所以在上面的计算时不再需要转换.
                stack.append(int(s))
        return stack.pop()