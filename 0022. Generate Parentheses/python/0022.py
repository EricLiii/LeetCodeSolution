class Solution_1:
"""
Runtime: 36 ms, faster than 93.66% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.

Idea:
回溯法.
Link: https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution
"""
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        string = ""
        #关键：将lst作为参数传递。
        "在python中，一切皆对象，Python参数传递采用的都是“传对象引用”的方式。"
        "实际上，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象(比如字典或者列表)"
        "的引用，就能修改对象的原始值，相当于通过“传引用”来传递对象。"
        "如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用,就不能直接修改原始对象，"
        "相当于通过“传值’来传递对象，此时如果想改变这些变量的值，可以将这些变量申明为全局变量。"
        #所以这里lst实际上是传引用。0091题中我曾尝试传引用一个int值结果失败了，就是因为int值是不可变对象。
        self.backtracking(lst, string, 0, 0, n)
        return lst
    
    def backtracking(self, lst, string, open, close, n):
        if len(string) == 2*n: #if close == n: 也可以.
            lst.append(string)
            return
        #注意，以下是if...if,不是if...else.
        if open < n:
            self.backtracking(lst, string+"(", open+1, close, n)
        if close < open: #注意这里是close < open, 不是close < n.
            self.backtracking(lst, string+")", open, close+1, n)
            
class Solution_2:
"""
Runtime: 40 ms, faster than 77.88% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.

Idea:
迭代. 但是没完全看懂，以后有时间再看.
Link: https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution.
"""
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]