class Solution_1:
"""
Author: Zefeng

Runtime: 36 ms, faster than 68.82% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.8 MB, less than 6.30% of Python3 online submissions for Pascal's Triangle.
"""
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2, numRows): #因为已经排除了一些情况，此时应该从2开始。
            tmp = [1]
            for j in range(1, len(res[-1])):
                tmp += [res[-1][j]+res[-1][j-1]]
            tmp += [1]
            res.append(tmp)
        return res

class Solution_2:
"""
Runtime: 36 ms, faster than 68.82% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.8 MB, less than 6.30% of Python3 online submissions for Pascal's Triangle.

Idea: 
    1 1            1 2 1        1 3 3 1
  +   1 1        +   1 2 1    +   1 3 3 1
  ---------      ---------    -----------
    1 2 1          1 3 3 1      1 4 6 4 1
"""
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        pascal=[[1]]
        for i in range(1,numRows):
            pascal.append([1])
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1+num2)
            pascal[-1].append(1)
        return pascal

class Solution_3:
"""
Runtime: 32 ms, faster than 89.79% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 6.30% of Python3 online submissions for Pascal's Triangle.

Idea:
这里将map()和lambda()结合使用：
1. The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
2. map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]): "lambda x, y: x+y" is the lambda function, it requires two arguments;
                                                        "res[-1] + [0]" is the first argument for lambda function;
                                                        "[0] + res[-1]" is the second argument for lambda function.
这道题主要记算法，即0121 和 1210 对应位相加即使下一行结果1331.

记这个!!!
"""
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            #这个lambda函数 将res[-1] + [0] 和 [0] + res[-1] 的对应位置相加.
            res.append(list((map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))))
            # OR res += [list((map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))]
        return res[:numRows] #这里考虑了edge case: input=0. 若input是0，应该返回[].
