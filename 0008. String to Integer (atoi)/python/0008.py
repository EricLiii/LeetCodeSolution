class Solution_1:
"""
Author: Zefeng

Runtime: 36 ms, faster than 91.85% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 5.24% of Python3 online submissions for String to Integer (atoi).
"""
    def myAtoi(self, str: str) -> int:
        lst = ["0", "1", "2", "3", "4",
               "5", "6", "7", "8", "9"]
        lst_ = ["-", "+"]
        res = 0
        flag = 1
        space = True
        for i in range(len(str)):
            if str[i] == " ":
                if space:
                    continue
                else:
                    break 
            elif str[i] in lst_:
                if str[i] == "-":
                    flag = -1
                    lst_ = []
                elif str[i] == "+":
                    flag = 1
                    lst_ = []
                space = False
            elif str[i] in lst:
                res = res*10 + int(str[i])
                
class Solution_2:
"""
Runtime: 36 ms, faster than 91.85% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 5.24% of Python3 online submissions for String to Integer (atoi).
"""
    def myAtoi(self, str: str) -> int:
        #由于除了开头的空格之外，中间出现空格也算invalid，
        #所以在solution_1中我用一个flag来判断空格是出现在数字前还是数字后。
        #其实这样是多余的，只要将str开头结尾的空格去掉，如果还有空额出现，那一定是invalid。
        #主要还是对strip()不熟。
        #Link： https://www.cnblogs.com/huangbiquan/p/7923008.html
        str=str.strip()
        neg=False
        if str and str[0] =='-':
            neg=True
        if str and (str[0]=='+' or str[0]=='-'):             
            str=str[1:]
        if not str:
            return 0
        
        digits={i for i in '0123456789'}
        # Or use isdigit() instead of dic to check if it is an integer, will be faster        
        result=0
        for c in str:
            if c not in digits:
                break
            result=result*10+int(c)
        if neg:
            result=-result
        #这样进行对overflow判断更加简洁。
        result=max(min(result,2**31-1),-2**31)
        return result
        
class Solution_3:
"""
Runtime: 36 ms, faster than 91.85% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 5.24% of Python3 online submissions for String to Integer (atoi).
"""
    def myAtoi(self, str: str) -> int:
        #变成列表，可以方便地去掉开头的"-"或"+".
        ls = list(str.strip())
        if len(ls) == 0 : return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + int(ls[i])
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
        
class Solution:
"""
Author: Zefeng
Runtime: 36 ms, faster than 92.50% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).

自己写的，不过有点繁琐.
"""
    def myAtoi(self, str: str) -> int:
        if not str or not str.strip(" "):
            return 0
        str = str.strip(" ")
        if str[0] == "+" or str[0] == "-":
            pos = 1 if str[0] == "+" else -1
            str = str[1:]
        elif str[0].isdigit():
            pos = 1
        else:
            return 0
        
        for i in range(len(str)):
            if not str[i].isdigit():
                str = str[:i]
                break
        if str:
            value = int(str)
        else:
            return 0
        if pos * value > 2**31 - 1:
            return 2**31-1
        elif pos * value < -2**31:
            return -2**31
        return pos * value
