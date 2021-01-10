class Solution:
"""
Runtime: 48 ms, faster than 42.35% of Python3 online submissions for Distinct Subsequences.
Memory Usage: 14.4 MB, less than 77.83% of Python3 online submissions for Distinct Subsequences.

https://www.cnblogs.com/zmyvszk/p/5511197.html

"""
    def numDistinct(self, s: str, t: str) -> int:
    
        #注意s,t在生成矩阵时的顺序，会影响后面遍历的顺序
        res = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            res[i][0] = 1
            
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
                else:
                    res[i][j] = res[i-1][j]
        return res[-1][-1]