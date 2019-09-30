class Solution:
"""
Runtime: 108 ms, faster than 5.51% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.4 MB, less than 11.53% of Python3 online submissions for Minimum Path Sum.

Idea: 
Calculate the path sum for first row and column respectively. 
"""
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
        
class Solution:
"""
还有一种可以只用O(n)空间的算法，暂时懒得想了，以后补上!!!

Link: https://leetcode.com/problems/minimum-path-sum/discuss/23613/Python-solutions-(O(m*n)-O(n)-space).
"""