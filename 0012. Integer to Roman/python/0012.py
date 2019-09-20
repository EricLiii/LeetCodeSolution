class Solution_1:
"""
Runtime: 48 ms, faster than 34.62% of Python online submissions for Integer to Roman.
Memory Usage: 11.8 MB, less than 31.25% of Python online submissions for Integer to Roman.

记这个，下面那个太tricky.
"""
    def intToRoman(self, num: int) -> str:
        #虽然名字叫mapping，但其实是一个list.
        mapping=[(1000,'M'),
                 (900,'CM'),
                 (500,'D'),
                 (400,'CD'),
                 (100,'C'),
                 (90,'XC'),
                 (50,'L'),
                 (40,'XL'),
                 (10,'X'),
                 (9,'IX'),
                 (5,'V'),
                 (4,'IV'),
                 (1,'I')]
        roman=[]
        for i, numeral in mapping:
            while num >= i:
                num -= i
                roman.append(numeral)
        return "".join(roman)
        
class Solution_2:
"""
Runtime: 36 ms, faster than 74.79% of Python online submissions for Integer to Roman.
Memory Usage: 11.7 MB, less than 83.59% of Python online submissions for Integer to Roman.
"""
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10];
        

