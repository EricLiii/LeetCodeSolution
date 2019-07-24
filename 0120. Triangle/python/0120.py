class Solution_1:
"""
Runtime: 68 ms, faster than 83.56% of Python3 online submissions for Triangle.
Memory Usage: 14.9 MB, less than 6.71% of Python3 online submissions for Triangle.

Link: https://blog.csdn.net/qq_38595487/article/details/82461657
"""
    def minimumTotal(self, triangle: List[List[int]]) -> int:    
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]