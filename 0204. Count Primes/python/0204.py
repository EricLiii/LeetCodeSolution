Link: https://blog.csdn.net/github_39261590/article/details/73864039

class Solution_1:
"""
Runtime: 264 ms, faster than 84.40% of Python3 online submissions for Count Primes.
Memory Usage: 37.1 MB, less than 37.93% of Python3 online submissions for Count Primes.
"""
    def countPrimes(self, n: int) -> int:
        if n < 3: #因为求的是小于n的质数，所以n=2时结果也是0.
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1): # n的最小的非质因子一定小于n的平方根.
            if primes[i]:
                #要从i的两倍开始，否则第i项也成False了。
                primes[i*2: n: i] = [False] * len(primes[i*2: n: i]) #仔细品这行!!
        return sum(primes)


class Solution_2:
"""
Runtime: 224 ms, faster than 88.03% of Python3 online submissions for Count Primes.
Memory Usage: 37.1 MB, less than 37.93% of Python3 online submissions for Count Primes.
"""
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            #其实没必要从i*2开始，因为i*2 = 2*i, 在i=2的时候已经处理过了.
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
    
