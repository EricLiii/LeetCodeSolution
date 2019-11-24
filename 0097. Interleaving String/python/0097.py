class Solution:
"""
Runtime: 36 ms, faster than 88.08% of Python3 online submissions for Interleaving String.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Interleaving String.

https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
"""
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        table = [[False]*(len(s2)+1)]*(len(s1)+1) #s1,s2顺序别错，不然不通过。TODO：想想为什么？
        table[0][0] = True
        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = table[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    table[i][j] = table[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
                    
        return table[-1][-1]