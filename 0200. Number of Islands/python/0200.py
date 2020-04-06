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
        
class Solution_2:
"""
Runtime: 188 ms, faster than 17.95% of Python3 online submissions for Number of Islands.
Memory Usage: 15.1 MB, less than 9.40% of Python3 online submissions for Number of Islands.

bfs.
"""
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        self.queue = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.queue.append((i, j))
                    self.bfs(grid)
                    count += 1
        return count
        
    def bfs(self, grid):
        while self.queue:
            i, j = self.queue.pop(0) #往后放，从头取.
            if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == "0":
                continue
            if grid[i][j] == "1":
                grid[i][j] = "0"
                self.queue += [item for item in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]]
                self.bfs(grid)
                
class Solution_3:
"""
Runtime: 168 ms, faster than 41.92% of Python3 online submissions for Number of Islands.
Memory Usage: 14.6 MB, less than 9.40% of Python3 online submissions for Number of Islands.

bfs,但是写在同一个函数里，更简洁.
"""
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = collections.deque()
        steps = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' : 
                    count+=1
                    grid[i][j] = '0'
                    queue.append((i,j))
                    while queue:
                        x,y = queue.popleft()
                        for step in steps:
                            if 0<= x+step[0]<len(grid) and 0<=y+step[1]<len(grid[0]) and grid[x+step[0]][y+step[1]] == '1':
                                grid[x+step[0]][y+step[1]] = "0"
                                queue.append((x+step[0] ,y+step[1]))
        return count
        
        
class Solution_4:
"""
Zefeng

Runtime: 208 ms, faster than 6.31% of Python3 online submissions for Number of Islands.
Memory Usage: 14.9 MB, less than 9.40% of Python3 online submissions for Number of Islands.

dfs
"""
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '-1'
                    self.dfs(grid, ((i+1,j), (i-1,j), (i,j+1), (i,j-1))) 
                    res += 1
        return res
                    
    def dfs(self, grid, candidates):
        for i, j in candidates:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '-1'
                self.dfs(grid, (((i+1,j), (i-1,j), (i,j+1), (i,j-1))))