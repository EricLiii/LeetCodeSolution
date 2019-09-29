class Solution_1:
"""
Runtime: 152 ms, faster than 5.24% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.3 MB, less than 5.25% of Python3 online submissions for Set Matrix Zeroes.

Idea: 
1. 首先检查第一行和第一列中有没有0.如果有，设置对应flag为True。但是此时不对矩阵进行修改。
2. 然后依次检查除了第一行和第一列的元素是否为0.如果为0，将对应的在第一行和第一列的位置设置为0.
3. 再在第一行和第一列中检查为0的元素，并进行修改。
4. 最后修改第一行和第一列。
"""
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        col_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0
                
                
class Solution_2:
"""
Runtime: 152 ms, faster than 80.05% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.3 MB, less than 5.13% of Python3 online submissions for Set Matrix Zeroes.

记这个!
"""
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            #因为这里用第一列作为标志，所以需要从后往前遍历，否则会污染标志.
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n