class Solution_1:
"""
Runtime: 36 ms, faster than 71.90% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 13.9 MB, less than 5.95% of Python3 online submissions for Fraction to Recurring Decimal.

Idea:
Link: https://www.cnblogs.com/ganganloveu/p/4170601.html

这题就是按定义做。

如果不能整除，就不断进行余数补零除以除数。

维护一个映射表m, 用来记录每个除数对应返回值ret中的位置。

（1）当出现重复的除数n时，说明找到了循环体，根据m[n]找到r中位置，加上相应的'('和')'将循环体括起来即可返回。

（2）当余数r为0时，返回ret。

注意点：

1、正负号

2、分子为0
"""
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator == 0:
            return str(numerator)
        if (numerator < 0) ^ (denominator < 0):
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        if (numerator % denominator == 0):
            return res
        res += "."
        r = numerator % denominator
        m = {}
        while r:
            if r in m:
                res = res[:m[r]] + "(" + res[m[r]:] + ")"
                break
            m[r] = len(res)
            r *= 10
            res += str(r // denominator)
            r %= denominator
        return res