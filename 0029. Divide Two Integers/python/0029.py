class Solution_1:
"""
Author: Zefeng

Runtime: 112 ms, faster than 5.84% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.8 MB, less than 5.62% of Python3 online submissions for Divide Two Integers.
"""
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        #以下判断语句也显得业余，见solution_2。    
        if (dividend > 0 and divisor >0) or (dividend < 0 and divisor <0):
            sign = 1
        else: 
            sign = -1
            
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        n = 1
        while n != 0:
            if dividend >= divisor*n:
                dividend -= divisor*n
                res += n
                n += 1
            else:
                n -= 1     
        #以后此类问题在返回时不要再用以下句式，显得业余：
        #return sign*res if sign*res <= pow(2,31)-1 and sign*res >= -pow(2,31) else pow(2,31)-1 
        return min(max(-pow(2,31), sign*res), pow(2,31)-1)


class Solution_2:
"""
This solution use << to reduce processing time.

Runtime: 44 ms, faster than 36.89% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.6 MB, less than 5.62% of Python3 online submissions for Divide Two Integers.
"""
    def divide(self, dividend: int, divisor: int) -> int:
        #记这种判断语句。
        #同时要注意, (dividend < 0 is divisor < 0)的写法是错的，必须分别用括号括起来.
        positive = (dividend < 0) is (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                #由于不能用*,所以这里用<<来完成乘2的操作。
                #<<方向别记翻; >>是除以2.
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
        
class BadSolution:      
"this solution will exceed time limitation"
    def divide(dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)     
    
"Maybe don't need return min(max(-2147483648, res), 2147483647), just return min(res, 2147483647) is accepted, too"   
"This is because there is no possibility that res is smaller than -2147483648 in this problem."
    
