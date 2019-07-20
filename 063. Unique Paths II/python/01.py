class Solution_1:
"""
Runtime: 56 ms, faster than 11.03% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.9 MB, less than 5.28% of Python3 online submissions for Unique Paths II.

Idea:
创建另一个矩阵来计算不同路径数量，obstacleGrid只用来检查是否行得通。
因为要考虑边界，所以创建的矩阵的行列都比obstacleGrid多1.
创建的矩阵先全部赋0，然后初始化其中一项以保证能正常累积。
举例：
obstacleGrid: [[0,0,0],
               [0,1,0],
               [0,0,0]]
dp:           [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
init dp as:   [[0,1,0,0],     or    [[0,0,0,0],
               [0,0,0,0],            [1,0,0,0],
               [0,0,0,0],            [0,0,0,0],
               [0,0,0,0]]            [0,0,0,0]]
这样的话，当obstacleGrid[0][0]不是障碍时，dp可以正常进行累积。      
"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
class Solution_2:
"""
Runtime: 68 ms, faster than 11.03% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.1 MB, less than 5.28% of Python3 online submissions for Unique Paths II.

An improved version of solution_1, save space, but the time complexity is still too long.
"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        
class Solution_3:
"""
There should be a faster solution, find it later!!!
"""