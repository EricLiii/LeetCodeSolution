class Solution:
"""
Runtime: 128 ms, faster than 26.13% of Python3 online submissions for N-Queens.
Memory Usage: 14.8 MB, less than 38.60% of Python3 online submissions for N-Queens.

https://leetcode.com/problems/n-queens/discuss/19808/Accepted-4ms-c%2B%2B-solution-use-backtracking-and-bitmask-easy-understand.
"""
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 这里不用['.'] * n, 直接用字符串就行
        board = ["." * n for _ in range(n)]
        self.board = board
        self.res = []
        self.solve(n, 0)   
        return self.res
        
        
    def solve(self, n, row):
        # 如果当前行是最后一行
        if row == n:
            # 这里必须copy self.board，因为直接append self.board的话只是将它的引用添加到self.res中。
            # 后面在恢复现场时，会将self.res中的也恢复.
            self.res.append(self.board.copy())
            return
        
        for j in range(n):
            # 不需要检查是否为"." or "Q"， 因为这是新的一行，必然全是"."
            # 只需检查当前位置所在的列上是否有"Q".
            # 而且只需要检查当前位置所在的列中在当前行之前的行。
            if self.valid(row, j, n):
                # python中字符串是不可改变的，所以不能通过self.board[row][col] = "Q"的方法将"."替换为"Q"
                # 也不能self.board[row][col:col+1] = "Q"
                # 只能新建一个字符串
                self.board[row] = self.board[row][:j] + "Q" + self.board[row][j+1:]
                # 因为是n皇后问题，而且同一行内不可能有两个皇后，所以一定是每一行一个皇后。
                # 当前行有皇后以后，直接到下一行。
                self.solve(n, row+1)
                # 恢复现场
                self.board[row] = self.board[row][:j] + "." + self.board[row][j+1:]
                    
                
    def valid(self, i, j, n):       
        # check all chars in column j
        for x in range(n):
            # 不必专门排除当前位置，因为此时还没有将"."替换为"Q"
            # if x == i:
            #     continue
            if self.board[x][j] == "Q":
                return False
        
        # 检查对角线时只需检查当前行之上的位置，因为下面必然还全是"."
        
        # check positive diagonal
        a, b = i-1, j-1
        while a >= 0 and b >= 0:
            if self.board[a][b] == "Q":
                return False
            else:
                a -= 1
                b -= 1
                
        # check positive diagonal
        a, b = i-1, j+1
        while a >= 0 and b < n:
            if self.board[a][b] == "Q":
                return False
            else:
                a -= 1
                b += 1
                
        return True