"这个题对时间，空间复杂度的要求很严格，所以我罗列了一些我写的、出问题的code."
class BadSolution_1:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return x
        
        sign = 1 if n > 0 else -1
        n = abs(n)
        e = 1
        res = 1
        while n != 0:
            if e <= n:
                #这里计算结果太大，溢出。
                res = res*x**e  
                n -= e
                e *= 2
            else:
                e //= 2
        if sign == 1:
            return sign*res
        else:
            return 1 / (sign*res)
            
class BadSolution_2:
"""
当输入为x=0.00001,n=2147483647时，超时。原因就是递归太多次了。
Solution_1对递归部分进行了改进，AC.
"""
    def myPow(self, x: float, n: int) -> float:
        if (n == 0): return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if (int(n % 2) == 0): 
            return self.myPow(x, int(n/2)) * self.myPow(x, int(n/2))
        else: 
            return x * self.myPow(x, int(n//2)) * self.myPow(x, int(n//2))
            
            
class Solution_1:
"""
Runtime: 36 ms, faster than 73.79% of Python3 online submissions for Pow(x, n).
Memory Usage: 14 MB, less than 6.21% of Python3 online submissions for Pow(x, n).

Idea: Recursive solution.
"""
    def myPow(self, x: float, n: int) -> float:
        if (n == 0): return 1
        if n < 0:
            #这里注意, 输入为1/x和-n.
            return self.myPow(1/x, -n)
        if (int(n % 2) == 0): 
            #这里当n时偶数的时候，将输入改为x*x,这样就减少一次递归。
            return self.myPow(x*x, n // 2)
        else: 
            #这里当n时奇数的时候，将n减一，这样n就成了偶数,在进行下一次判断时，输入会变成x*x.
            #相比BadSolution_2,也减少了一次递归。
            return x * self.myPow(x, n-1)
            
class Solution_2:
"""
Runtime: 36 ms, faster than 73.79% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 6.21% of Python3 online submissions for Pow(x, n).

Idea:
Iterative solution. 
快速幂算法,值得学习！ https://www.cnblogs.com/sun-of-Ice/p/9330352.html
"""
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            # &是按位与操作.如果n是奇数,n&1为0;如果n是偶数,n&1为1.
            # 这个是快速幂算法。
            if n & 1:
                pow *= x
            x *= x
            n >>= 1 #右移操作,以便于检查下一位是否为1.
        return pow
"需要注意的是，由于n的范围是-2**31~2**31-1，所以当n是-2**31的时候，n=-n将超出范围。"
"虽然python中不会溢出，但是在c++中要额外考虑这种情况"