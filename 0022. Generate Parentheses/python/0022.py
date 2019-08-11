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
        self.backtracking(lst, string, 0, 0, n)
        return lst
    
    def backtracking(self, lst, string, open, close, n):
        if len(string) == 2*n:
            lst.append(string)
            return
        #注意，以下是if...if,不是if...else.
        if open < n:
            self.backtracking(lst, string+"(", open+1, close, n)
        if close < open:
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