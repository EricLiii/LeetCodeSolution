class Solution:
"""
Author: Zefeng

Runtime: 32 ms, faster than 96.36% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.8 MB, less than 5.94% of Python3 online submissions for Spiral Matrix II.

Idea:
Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.
"""
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        return self.fill(res, 1, 0, 0, n)

    def fill(self, nums, count, row, col, n):
        while count <= n*n:
            while col < n and nums[row][col] == 0:
                nums[row][col] = count
                count += 1
                col += 1
            col -= 1
            row += 1
            while row < n and nums[row][col] == 0:
                nums[row][col] = count
                count += 1
                row += 1
            row -= 1
            col -= 1
            while col < n and nums[row][col] == 0:
                nums[row][col] = count
                count += 1
                col -= 1
            col += 1
            row -=1
            while row < n and nums[row][col] == 0:
                nums[row][col] = count
                count += 1
                row -= 1
            row += 1
            col += 1
        return nums


class Solution_2:
"""
Runtime: 36 ms, faster than 81.69% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14 MB, less than 5.94% of Python3 online submissions for Spiral Matrix II.

Idea: 
Same idea with solution 1, but more concise!
"""
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1 
        # di, dj represent the increment of i and j.
        for k in range(n*n):
            matrix[i][j] = k + 1
            # 这里实现向右转的方法非常巧妙：
            # 以第一行为例，当给m[0][0]赋值时，检查m[0][1]是否为零;
            #               当给m[0][1]赋值时，检查m[0][2]是否为零;
            #               当给m[0][2]赋值时，检查m[0][0]是否为零.
            #                   m[0][0]已经被赋值过，所以更新di, dj.
            #                   这样就相当于实现了向右转。
            if matrix[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return matrix
        
class Solution_3:
"""
Use the method in Spiral Matrix, preformance is not good enough but is still worth to learn.
I also try to do so but failed. The reason is I didn't come up with the idea that saving coordinates in matrix.

Runtime: 40 ms, faster than 55.42% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.9 MB, less than 5.94% of Python3 online submissions for Spiral Matrix II.

Idea:
(1) Create a matrix to store the coordinates

    (0,0) (0,1) (0,2)

    (1,0) (1,1) (1,2)

    (2,0) (2,1) (2,2)

(2) Read it out using the trick of "Spiral Matrix I"

    (0,0) (0,1) (0,2) (1,2) (2,2) ...

(3) Put 1, 2, 3, ... n**2 at these coordinates sequentially. Done.
"""
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        coord = [[(i,j) for j in range(n)] for i in range(n)]
        count = 1
        while coord:
            for item in list(coord.pop(0)):
                result[item[0]][item[1]] = count
                count += 1
            coord = [*zip(*coord)][::-1]

        return result
        
        
class Solution_4:
"""
Fucking genious!

Runtime: 36 ms, faster than 81.69% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14 MB, less than 5.94% of Python3 online submissions for Spiral Matrix II.

Idea:
Start with the empty matrix, add the numbers in reverse order until we added the number 1. Always rotate the matrix clockwise and add a top row.
    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
Details:
    matrix         |      low       |        high
    ----------------------------------------------------
    []                    10                  10
    ----------------------------------------------------
    [[]]                   9                  10
    ----------------------------------------------------
    [[9]]                  8                   9
    ----------------------------------------------------
    [[8],                  6                   8
     (9,)]
    ----------------------------------------------------
    [[6,7],                4                   6
     (9,8)]
    ----------------------------------------------------
    [[4,5],                1                   4
     (9,6),
     (8,7)]
    ----------------------------------------------------
    [[1,2,3],
     (8,9,4),             -2                   1
     (7,6,5)]
    
"""
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, low = [], n*n+1
        while low > 1:
            low, high = low - len(matrix), low
            matrix = [list(range(low, high))] + list(zip(*matrix[::-1]))
            # note, []+()=()
        return matrix