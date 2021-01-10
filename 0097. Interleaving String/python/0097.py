class Solution:
"""
Runtime: 36 ms, faster than 88.08% of Python3 online submissions for Interleaving String.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Interleaving String.

https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
"""
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        #s1,s2的顺序如果变了，之后的s1,s2都要变
        table = [[False]*(len(s2)+1)]*(len(s1)+1) 
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
                    # 即使连续从s1,s2中的一个取了字符也没关系，因为可以将这两个字符合并为取一次，故仍然满足interleaving的原则。
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
                    
        return table[-1][-1]