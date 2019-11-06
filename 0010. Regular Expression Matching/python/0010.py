class Solution_1:
"""
Runtime: 60 ms, faster than 60.10% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.6 MB, less than 5.55% of Python3 online submissions for Regular Expression Matching.

https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

没掌握, 以后有时间再看看.
"""
    def isMatch(self, s: str, p: str) -> bool:   
        # link中先判断s,p是否有一个为empty.但是我用python实现的时候这一步是多余的，会报错。
        # 但是link中用java实现却不会报错。
        # TODO: 以后有时间想一想怎么回事.
        
        
        m, n = len(s), len(p)
        #注意，要想创建m+1行需要将m+1在外面循环。顺序不要搞错.
        M = [[False for i in range(n+1)] for j in range(m+1)] 
        M[0][0] = True 
        
        for j in range(2, n+1, 2):
            if p[j-1] == "*" and M[0][j-2]:
                M[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                curS, curP = s[i-1], p[j-1]
                if curS == curP or curP == ".":
                    M[i][j] = M[i-1][j-1]
                elif curP == "*":
                    preCurP = p[j-2]
                    if preCurP != "." and preCurP != curS:
                        M[i][j] = M[i][j-2]
                    else:
                        M[i][j] = M[i][j-2] or M[i-1][j-2] or M[i-1][j]
        return M[m][n]