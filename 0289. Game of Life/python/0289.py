class Solution_1:
"""
Runtime: 32 ms, faster than 61.00% of Python3 online submissions for Game of Life.
Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Game of Life.

https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
"""
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = self.neighbors(board, i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
                
                
                
    def neighbors(self, board, i, j):
        lives = 0
        #这里注意由于使用range,为了能取到i+1,应该代入i+1+1.
        for x in range(max(0, i-1), min(i+1+1, len(board))):
            for y in range(max(0, j-1), min(j+1+1, len(board[0]))):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives