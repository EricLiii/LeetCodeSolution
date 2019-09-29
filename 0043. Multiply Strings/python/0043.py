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
        
class Solution_2:
"""
Simplify solution_1.

Runtime: 280 ms, faster than 7.73% of Python3 online submissions for Multiply Strings.
Memory Usage: 14 MB, less than 5.66% of Python3 online submissions for Multiply Strings.
"""
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return 0
        lst = []
        lst2 = []
        res = 0
        n = e = 0
        for i in range(len(num1)-1, -1, -1):
            n = 0
            for j in range(len(num2)-1,-1, -1):
                res += int(num1[i])*int(num2[j])*10**n*10**e
                n += 1
            e += 1
        return str(res)
        
class Solution_3:
"""
记这个!!!

Runtime: 160 ms, faster than 37.78% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.7 MB, less than 5.68% of Python3 online submissions for Multiply Strings.

Link:
https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
"""
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return "0"
        res = "0"
        lst = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1): #记住从后往前遍历的写法.
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i+j, i+j+1
                summ = mul + lst[p2]
                #这里注意p1处要加上之前的值，p2处直接替换。
                #what if pos[p1] == 9 and sum > 10 ?  discussion里有解答. 
                lst[p1] += summ // 10
                lst[p2] = summ % 10
        res = "".join(map(str, lst))
        #lstrip(): 避免"01","001",...等情况出现。
        #int(res): 避免"0","00","000",..等情况出现。
        res = res.lstrip("0") if int(res) != 0 else "0"
        return res