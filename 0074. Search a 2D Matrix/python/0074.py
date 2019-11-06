class Solution_1:
"""
Author: Zefeng

Runtime: 72 ms, faster than 8.99% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15.9 MB, less than 5.34% of Python3 online submissions for Search a 2D Matrix.

Idea:
Divide and conquer
"""
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if len(matrix) == 1:
            for item in matrix[0]:
                if item == target:
                    return True
            return False
        fir = len(matrix) // 2
        # 要注意这里，应该是fir-1而不是fir。
        if target > matrix[fir-1][-1] and target < matrix[fir][0]:
            return False
        elif target == matrix[fir-1][-1] or target == matrix[fir][0]:
            return True
        else:
            if target < matrix[fir-1][-1]:
                return self.searchMatrix(matrix[:fir], target)
            else:
                return self.searchMatrix(matrix[fir:], target)

class Solution_2:
"""
Author: Zefeng

Runtime: 80 ms, faster than 9.68% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15.9 MB, less than 5.34% of Python3 online submissions for Search a 2D Matrix.

Idea:
Improve solution_1, but still bad time complexity.
"""
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if len(matrix) == 1:
            return self.binSearch(matrix[0], target)
        fir = len(matrix) // 2
        if target > matrix[fir-1][-1] and target < matrix[fir][0]:
            return False
        elif target == matrix[fir-1][-1] or target == matrix[fir][0]:
            return True
        else:
            if target < matrix[fir-1][-1]:
                return self.searchMatrix(matrix[:fir], target)
            else:
                return self.searchMatrix(matrix[fir:], target)
    
    def binSearch(self, nums, target):
        if not nums:
            return False
        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False
        fir = len(nums) // 2
        if target > nums[fir-1] and target < nums[fir]:
            return False
        elif target == nums[fir-1] or target == nums[fir]:
            return True
        else:
            if target < nums[fir-1]:
                return self.binSearch(nums[:fir], target)
            else: 
                return self.binSearch(nums[fir:], target)

class Solution_3:
"""
Runtime: 68 ms, faster than 9.68% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15.7 MB, less than 5.34% of Python3 online submissions for Search a 2D Matrix.

Idea:
Same with solution_2, but shorter. Because solution_2 is recursive solution while this is iterative solution. 
In solution_2 I have to define a new function to handle the situation where the length of nums is one.
"""
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False