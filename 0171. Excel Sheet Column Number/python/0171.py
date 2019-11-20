class Solution_1:
"""
Author: Zefeng

Runtime: 48 ms, faster than 8.67% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Excel Sheet Column Number.
"""
    def titleToNumber(self, s: str) -> int:
        #生成0~25的数列
        lst = [chr(x) for x in range(ord("A"), ord("Z")+1)]
        #将数列转化为字典，key是字母，value是数字。
        dic = {letter:lst.index(letter) for letter in lst}
        res = 0
        for i in range(len(s)):
            #关键是dic[s[i]]+1,别忘了加1.
            res += (dic[s[i]]+1)*26**(len(s)-1-i)
        return res
        
class Solution_2:
"""
Improve solution_1.

Runtime: 40 ms, faster than 58.77% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Excel Sheet Column Number.
"""
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        summ = 0
        #enumerate!还是不熟!!!
        for exp, char in enumerate(s):
            summ += (ord(char) - 65 + 1) * (26 ** exp)
        return summ
        
class Solution_3:
"""
Runtime: 40 ms, faster than 58.77% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Excel Sheet Column Number.
"""
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            #这样做连enumerate都不需要了！！！
            res = res*26 + ord(i)-ord('A')+1
        return res