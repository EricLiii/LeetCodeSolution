class Solution_1:
"""
这才叫pythonic coding！

Runtime: 28 ms, faster than 97.08% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.2 MB, less than 43.09% of Python3 online submissions for Spiral Matrix.
"""
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
"""
Explanation:
Eg, matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]
1. 思路是先将第一行pop输出，然后递归逆时针旋转90°后的矩阵：
    spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    = [1, 2, 3] + spiral_order([[6, 9],
                                [5, 8],
                                [4, 7]])

    = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                         [5, 4]])

    = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                                  [5]])

    = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

    = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

    = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

    = [1, 2, 3, 6, 9, 8, 7, 4, 5]
2. *的作用：将列表拆分为单个元素（只进行到第一层深度）：
    matrix.pop(0) = [1,2,3]
    print(*matrix.pop(0)) -> 1 2 3
    print(*matrix) -> [1,2,3] [4,5,6] [7,8,9]
    注意：不能直接写 *matrix，这样会报错。
3. zip的作用：
   zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
   如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
   Eg,
   matrix = [[4,5,6],
             [7,8,9]]
   (1)由于我们想处理的是matrix的两个子列表，所以此时需要用*将matrix分解。
      zip(*matrix) 会将[4,5,6]和[7,8,9]对应维度拼接成元组，即(4,7),(5,8)和(6,9)。
   (2)但是需要注意的是，zip()返回的是一个zip类型的object，如果我们想输出其中的元素，有两种办法：
      一是用list()函数将其转化为列表
      print(list(zip(*matrix))) >> [(4,7),(5,8),(6,9)]; 
      二是用*号将其分解：
      *zip(*matrix) >> (4,7) (5,8) (6,9) (注意：*zip(*matrix)会报错，这里只是为了说明才这样写)。
      print(*zip(*matrix)) >> (4,7) (5,8) (6,9)
      print([*zip(*matrix)]) >> [(4,7),(5,8),(6,9)]
4. [::-1]是逆序排列：matrix = [[4,7],
                               [5,8],
                               [6,9]]
                     matrix[::-1] = [[6,9],
                                     [5,8],
                                     [4,7]]
   这样就完成了对matrix的第一行进行pop后再逆时针旋转90°的操作。
5. matrix 后面的and的作用：
   (1)当matrix为[]时，返回[]
   (2)当matrix不为[]时，返回的是and后面的数据。因为实验表明，当list和tuple有冲突时，tuple有优先权：
      [[1,2,3],[4,5,6],[7,8,9]] and [[1,2,3],(6,9),(8,7),(4,),(5,)] -> [[1,2,3],(6,9),(8,7),(4,),(5,)]
      这样就既考虑了matrix为空的情况又不会影响matrix不为空的情况。
6. [*matrix.pop(0)] 的作用： 
   (1)第一次pop时，得到的是[1,2,3]，matrix=[[4,5,6],[7,8,9]]
   (2)之后对matrix进行了处理，带入到下一层迭代的是[(6,9),(5,8),(4,7)]
   (3)第二次pop时得到的是(6,9)。这样问题就来了，已知spiralOrder()函数返回的是list，list和tuple是不能直接拼接的，
      所以就要将pop出来的数据进行处理。
   (4)处理方法为：用[]将pop出的数据转换为list类型。
   (5)*的作用：如果不加*，最后结果将是[[1, 2, 3], (6, 9), (8, 7), (4,), (5,)]，所以需要用*将每个pop出的数据
      分解。
"""


class Solution_2:
"""
相比之下这个就容易理解多了.

Runtime: 32 ms, faster than 86.87% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.1 MB, less than 84.28% of Python3 online submissions for Spiral Matrix.
"""
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret