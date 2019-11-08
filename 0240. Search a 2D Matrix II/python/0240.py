class Solution:
"""
Runtime: 32 ms, faster than 99.18% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.5 MB, less than 81.48% of Python3 online submissions for Search a 2D Matrix II.
"""
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            row, col, width = len(matrix)-1, 0, len(matrix[0])
            while row >= 0 and col < width:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    row = row-1
                else:
                    col = col+1
        return False
