class Solution_1:
"""
Runtime: 620 ms, faster than 42.54% of Python3 online submissions for Combinations.
Memory Usage: 15.5 MB, less than 13.33% of Python3 online submissions for Combinations.

Link: https://leetcode.com/problems/combinations/discuss/27002/Backtracking-Solution-Java

太慢了.
"""
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        res = []
        self.helper(n, k, 1, [], res)
        return res
    
    def helper(self, n, k, start, path, res):
        if k == 0:
            res.append(path)
        for i in range(start, n+1):
            self.helper(n, k-1, i+1, path+[i], res)
            
class Solution_2:
"""
Runtime: 424 ms, faster than 63.06% of Python3 online submissions for Combinations.
Memory Usage: 15.4 MB, less than 16.67% of Python3 online submissions for Combinations.

Link: https://leetcode.com/problems/combinations/discuss/26992/Short-Iterative-C%2B%2B-Answer-8ms
"""
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        i = 0
        p = [0 for _ in range(k)]
        while i >= 0:
            p[i] += 1
            if p[i] > n:
                i -= 1
            elif i == k-1:
                #注意这里不能直接append(p).
                #因为在python中append是添加一个引用,如果单纯append(p),之后对p的改变同样会影响res中的元素。
                #因此要copy一个新的list,再append.
                
                #Link中是用c++写的，在c++中，push_back不是添加引用而是copy,所以它可以不用手动进行copy.
                res.append(list(p))
            else:
                i += 1
                p[i] = p[i-1]
        return res
        
class Solution_3:
"""
Runtime: 100 ms, faster than 90.53% of Python3 online submissions for Combinations.
Memory Usage: 15.3 MB, less than 30.00% of Python3 online submissions for Combinations.

Link: https://leetcode.com/problems/combinations/discuss/27029/AC-Python-backtracking-iterative-solution-60-ms

非常快, 但是没细看
以后有时间补上!!!
"""
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1