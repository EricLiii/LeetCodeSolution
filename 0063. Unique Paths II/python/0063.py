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
Runtime: 64 ms, faster than 10.97% of Python3 online submissions for Unique Paths II.
Memory Usage: 14 MB, less than 8.89% of Python3 online submissions for Unique Paths II.

Link: https://leetcode.com/problems/unique-paths-ii/discuss/23250/Short-JAVA-solution

与solution_2一样，稍微更简单一点.
"""

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0] * width
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(len(row)):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]
        
class Solution_4:
"""
Author: Zefeng

Runtime: 52 ms, faster than 85.04% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.9 MB, less than 8.89% of Python3 online submissions for Unique Paths II.

和solution_2思路一样，只不过没有添加额外的行和列。
这个solution和0062的解法很像，所以容易记。
但是多用了两个for loop来初始化matrix，比较麻烦，所以最好还是记solution_2。

另外，和0062一样，只需要保证第一行和第一列的初始化时正确的就行，其他位置的值在后面会改变。
"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0 for row in range(n)] for col in range(m)]
        for i in range(len(matrix)):
            if obstacleGrid[i][0] != 1:
                matrix[i][0] = 1
            else:
                break
                
        for i in range(len(matrix[0])):
            if obstacleGrid[0][i] != 1:
                matrix[0][i] = 1
            else:
                break
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                matrix[i][j] = matrix[i][j-1]+matrix[i-1][j]
        return matrix[-1][-1]