class NumMatrix:
"""
Runtime: 112 ms, faster than 88.74% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 15.9 MB, less than 66.67% of Python3 online submissions for Range Sum Query 2D - Immutable.

https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution
"""
    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [ [0 for j in range(m+1)] for i in range(n+1) ]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]
