class Solution_1:
"""
Runtime: 68 ms, faster than 98.90% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.8 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.

Fast.

Link: https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.

因为每次maxlen的增加只会是1或者2，对应的start可能是i - maxLen或者i - maxLen - 1.
因此情况a先判断在i-maxLen可以减1的情况下是否有新的最长回文。
情况b则是判断在i-maxLen不能减1的情况下是否有新的最长回文.
"""
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
        	return ""
        maxLen = 1
        start = 0
        for i in range(len(s)):
            #a
        	if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
        		start = i - maxLen - 1
        		maxLen += 2
            #b
        	elif i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
        		start = i - maxLen
        		maxLen += 1
        return s[start:start+maxLen]
        
class Solution_2:
"""
Runtime: 980 ms, faster than 69.26% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 21.85% of Python3 online submissions for Longest Palindromic Substring.

Idea:
从中间向两边查找。

Slow,I think it's because this solution tranverse the string twice to make sure that 
palindorme substring can be found in both odd and even cases.
"""
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
        
class Solution_3:
"""
Runtime: 2572 ms, faster than 44.28% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 21.4 MB, less than 9.25% of Python3 online submissions for Longest Palindromic Substring.

Idea:
动态规划,虽然很慢,但是思路值得借鉴。
Link: https://blog.csdn.net/zxzxzx0119/article/details/81483564
此link是从后往前找的，我改为了从前往后找.
"""
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) < 2:
        	return s
        row = col = 0
        #这里需要注意的是：(1)[[False]*len(s) for _ in range(len(s))] 和 (2)[[False]*len(s)]*len(s)
        #虽然都会生成一个5*5的初始值均为False的矩阵，但是对他们进行相同的操作可能的得到不同的结果。
        #例如：dp[0][2],在(1)中，只有dp[0][2]的值会变为True,而在(2)中，每一行的第二个值都变成了True.
        #要记住这个区别，以后用得着.
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > col-row+1:
                        row = j
                        col = i
        return s[row:col+1]

class Solution_4:
"""
Manacher’s Algorithm: https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/

有时间一定要啃一下这个算法。

曼彻斯特!
"""