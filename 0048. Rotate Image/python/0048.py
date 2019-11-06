class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 83.25% of Python3 online submissions for Rotate Image.
Memory Usage: 13.3 MB, less than 21.90% of Python3 online submissions for Rotate Image.

Idea:
先求矩阵的转置，然后将每一行逆序排列即可。
"""
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for item in matrix:
            item.reverse()