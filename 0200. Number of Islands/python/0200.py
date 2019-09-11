class Solution_1:
"""
Runtime: 160 ms, faster than 63.76% of Python3 online submissions for Number of Islands.
Memory Usage: 14.9 MB, less than 9.40% of Python3 online submissions for Number of Islands.

dfs.
"""
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '0':
            return
        #遇见一个1就将它变成0，并且再调用dfs，将与它相邻的1也变成0。
        #这样就消除了一块陆地，之后numIslands中的遍历会再找下一块陆地.
        grid[i][j] = '0'  
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)