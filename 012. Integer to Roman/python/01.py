class Solution:
    def intToRoman(self, num: int) -> str:
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
            while num>=i:
                num-=i
                roman.append(numeral)
        return "".join(roman)
        
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10];
