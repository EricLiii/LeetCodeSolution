class BadSolution:
"""
Author: Zefeng

I think this is a right solution, but the time complexity is too long.
Time Limit Exceeded when test case is (23,12).
"""
    def uniquePaths(self, m: int, n: int) -> int:
        return self.find(n-1, m-1)
    
    def find(self, n, m):
        if n == 0 and m == 0:
            return 1
        if n < 0 or m < 0:
            return 0
        return self.find(n, m-1) + self.find(m, n-1)
        
class Solution_1:
"""
Runtime: 40 ms, faster than 23.58% of Python3 online submissions for Unique Paths.
Memory Usage: 13.9 MB, less than 5.18% of Python3 online submissions for Unique Paths.
"""
    def uniquePaths(self, m: int, n: int) -> int:
        #这里只要保证matrix的第一行和第一列全是1就行，其他位置的值在后面都会更新.
        matrix = [[1 for row in range(n)] for col in range(m)]
        # 因为只能向右走或者向下走，所以第一行的元素到第二行对应元素只有一种方法;
        # 同理第一列元素到第二列对应元素也只有一种方法;
        # 因此range可以从1开始计。
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1]+matrix[i-1][j]
        return matrix[-1][-1]
        
class Solution_2:
"""
Runtime: 32 ms, faster than 89.89% of Python3 online submissions for Unique Paths.
Memory Usage: 13.8 MB, less than 5.18% of Python3 online submissions for Unique Paths.

Idea:
This is an improved version of solution_1 using same idea.
"""
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0
        
class Solution_3:
"""
Idea:
这其实就是一个组合问题。对于一个m*n矩阵，要想到达终点需要向下走m-1步，向右走n-1步，一共走了m+n-2步。
不同的走法就有C(m-1, m+n-2)种。
"""
