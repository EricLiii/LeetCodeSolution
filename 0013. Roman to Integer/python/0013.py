class Solution_1:
"""
Runtime: 100 ms, faster than 6.11% of Python online submissions for Roman to Integer.
Memory Usage: 11.7 MB, less than 57.94% of Python online submissions for Roman to Integer.

This is a very slow solution.
"""
    def romanToInt(self, s: str) -> int:
        mapping={1000:'M',
                  900:'CM',
                  500:'D',
                  400:'CD',
                  100:'C',
                  90:'XC',
                  50:'L',
                  40:'XL',
                  10:'X',
                  9:'IX',
                  5:'V',
                  4:'IV',
                  1:'I'}
        num=0
        i=0
        while i<len(s):
            if i<len(s)-1:
                if s[i:i+2] in mapping.values():
                    num+=list(mapping.keys())[list(mapping.values()).index(s[i:i+2])]
                    i+=2
                else:
                    num+=list(mapping.keys())[list(mapping.values()).index(s[i])]
                    i+=1
            else:
                num+=list(mapping.keys())[list(mapping.values()).index(s[i])]
                i+=1
        return num
       
class Solution_2:
"""
记这个和solution_3.

Runtime: 24 ms, faster than 98.81% of Python online submissions for Roman to Integer.
Memory Usage: 11.6 MB, less than 86.11% of Python online submissions for Roman to Integer.

This one is faster because exchange the keys and values.
"""
    def romanToInt(self, s: str) -> int:
        mapping={ 'M':1000,
                'CM':900,
                'D':500,
                'CD':400,
                'C':100,
                'XC':90,
                'L':50,
                'XL':40,
                'X':10,
                'IX':9,
                'V':5,
                'IV':4,
                'I':1}
        num=0
        i=0
        while i<len(s):
            if i<len(s)-1 and s[i:i+2] in mapping:
                num+=mapping[s[i:i+2]]
                i+=2
            else:
                num+=mapping[s[i]]
                i+=1
        return num
        
class Solution_3:
"""
记这个和solution_2.

Runtime: 60 ms, faster than 34.64% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.1 MB, less than 5.40% of Python3 online submissions for Roman to Integer.

Idea:
The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.

当出现两个字母代表一个数字的情况时，前一个字母代表的数字一定小于后一个字母代表的数字。
所以当roman[s[i]] < roman[s[i+1]],一定是需要用两个字母代表一个数字。
同时两个字母代表一个数字时，其实等于后一个字母代表的数字减去前一个字母代表的数字;
即相当于z先减去前一个字母代表的数字，再加上后一个字母代表的数字。
"""
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
