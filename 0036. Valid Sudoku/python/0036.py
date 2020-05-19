class Solution_1:
"""
Runtime: 108 ms, faster than 75.06% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 5.53% of Python3 online submissions for Valid Sudoku.
"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and
        self.is_col_valid(board) and
        self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        # *将board打散，zip拼接。
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        
        
class Solution_2:
"""
Runtime: 100 ms, faster than 95.53% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 5.53% of Python3 online submissions for Valid Sudoku.

Idea:
Link: https://leetcode.com/problems/valid-sudoku/discuss/15464/My-short-solution-by-C%2B%2B.-O(n2)
"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        used1, used2, used3 = [[0]*9 for i in range(0,9)], [[0]*9 for i in range(0,9)], [[0]*9 for i in range(0,9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    k = i//3*3 + j//3
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        return False
                    used1[i][num] = used2[j][num] = used3[k][num] = 1
        return True
        
        
class Solution_3:
"""
Zefeng

Runtime: 224 ms, faster than 5.03% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Valid Sudoku.

作为与solution_2的比较，加深理解
"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 这里[0 for i in range(9)]是没必要的,因为0是静态变量,是复制
        # 而[0 for i in range(9)]初始化了一个列表，不能简单地用*,否则是引用.
        # 这点要与solution_2作比较。
        rows = [[0 for i in range(9)] for j in range(9)]
        cols = [[0 for i in range(9)] for j in range(9)]
        cells = [[0 for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                if self.check_rows(val, i, j, rows) and self.check_cols(val, i, j, cols) and self.check_cells(val, i, j, cells):
                    continue
                else:
                    return False
        return True
                            
    # solution_2的检查方法更简洁!
    def check_rows(self, val, i, j, rows):
        if val not in rows[i]:
            rows[i][val-1] = val
            return True
        else:
            return False

    def check_cols(self, val, i, j, cols):
        if val not in cols[j]:
            cols[j][val-1] = val
            return True
        else:
            return False

    def check_cells(self, val, i, j, cells):
        k = (i//3)*3 + (j//3)
        if val not in cells[k]:
            cells[k][val-1] = val
            return True
        else:
            return False
            