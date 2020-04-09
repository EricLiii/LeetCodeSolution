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
        
class Solution_1_WRONG:
"""
Zefeng

这道题不能用两个二分法查找，因为input的性质和以前不一样了(仔细想想).
这就是我为什么出错的原因!
"""
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        l, r = 0, len(matrix)-1
        while l < r:
            mid =  (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid
                
        ll, rr = 0, len(matrix[l])
        while ll < rr:
            mid = (ll+rr)//2
            if matrix[l][mid] == target:
                return True
            elif matrix[l][mid] > target:
                rr = mid-1
            else:
                ll = mid
        return False
