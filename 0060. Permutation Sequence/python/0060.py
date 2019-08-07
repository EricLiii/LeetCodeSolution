class Solution_1:
"""
Author: Zefeng

Runtime: 36 ms, faster than 76.52% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.5 MB, less than 7.32% of Python3 online submissions for Permutation Sequence.

Idea:
判断是第几个数字作为开头，进行递归。
"""
    def getPermutation(self, n: int, k: int) -> str:
        lst = [i+1 for i in range(n)]
        res = self.helper(lst, k)
        for i in range(len(res)):
            res[i] = str(res[i])
        res = "".join(res)
        return res
        
    def helper(self, lst, k):
        # 易证lst的长度一定是偶数。
        if not lst:
            return []
        if len(lst) == 2:
            return [lst[0], lst[1]] if k == 1 else [lst[1], lst[0]]
        le = len(lst)
        t = 1
        for i in range(le):
            t *= i+1
        b = int(t/le)
        count = 1
        while k > b*count:
            count += 1
        return [lst.pop(count-1)] + self.helper(lst, k-b*(count-1))
        
        
import math
class Solution_2:
"""
Runtime: 32 ms, faster than 94.21% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.8 MB, less than 7.32% of Python3 online submissions for Permutation Sequence.

Link: https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation
"""
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [*range(1, n+1)] #这个生成方法要记。
        permutation = ''
        #减一保证访问列表时不超出范围。
        k -= 1
        while n > 0:
            #减1是关键。
            n -= 1
            #math.factorial(n)求的是每个数字分别做开头时permutation的个数。
            #例如，n=4，每个数字做开头有6组permutation。
            #其实跟我的思想时一致的，但是实现更简洁。
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation