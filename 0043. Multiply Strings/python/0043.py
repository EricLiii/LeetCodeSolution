class Solution_1:
"""
Author: Zefeng

Runtime: 196 ms, faster than 17.56% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.7 MB, less than 5.66% of Python3 online submissions for Multiply Strings.

Idea:
根据乘法竖式来逐步计算: 
第一个数字的末位分别乘第二个数字的每一位;
第一个数字的倒数第二位分别乘第二个数字的每一位;
......
"""
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return 0
        lst = []
        lst2 = []
        while num1:
            lst.append(int(num1[-1]))
            num1 = num1[:-1]
        while num2:
            lst2.append(int(num2[-1]))
            num2 = num2[:-1]
        res = 0
        n = e = 0
        # lst和lst2谁长谁短不影响结果。
        for x in lst:
            n = 0
            for y in lst2:
                # 当第一个数字的末位跟第二个数字的每一位相乘时，e始终为0，n相应变化。
                # 当第一个数字的倒数第二位跟第二个数字的每一位相乘时，e始终为1，n相应变化。
                #       这是因为此时第一个数字的倒数第二位是以10为单位的。
                # 以此类推。
                res += x*y*10**n*10**e
                n += 1
            e += 1
        return str(res)