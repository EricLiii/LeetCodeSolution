class Solution_1:
"""
Runtime: 36 ms, faster than 87.11% of Python3 online submissions for Decode Ways.
Memory Usage: 13.8 MB, less than 16.00% of Python3 online submissions for Decode Ways.

Idea:
类似于0062和0070.
只不过0070每次肯定能爬1步或者2步，但是这个题需要进行判断.


Link：https://leetcode.com/problems/decode-ways/discuss/347813/readable-python-dp-7-lines-with-the-best-detailed-explanation-of-the-logic
这个链接中使用了result = (last_two not in [10, 20])*prev + (10 <= last_two <= 26)*prev_prev
更简洁，无需给tmp分配空间.
"""
    def numDecodings(self, s: str) -> int:
        if s == "": return 0
        prep, pre = 0, 1
        for i in range(len(s)):
            tmp = 0
            #注意两个if是并列的.
            if s[i] > "0":
                tmp += pre
            if s[i-1:i+1] < "27" and s[i-1:i+1] > "09":
            #下面这行会加快计算速度.
            #if i > 0 and s[i-1:i+1] < "27" and s[i-1:i+1] > "09": 
                tmp += prep
            prep = pre
            pre = tmp
        return pre