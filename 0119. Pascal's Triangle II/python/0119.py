class Solution_1:
"""
Runtime: 40 ms, faster than 20.55% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 14 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.

Idea:
先根据rowIndex生成pascal's triangle,然后返回最后一行.
"""
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(1, rowIndex+1):
            res.append(list((map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))))
        return res[rowIndex]



class Solution_2:
"""
Runtime: 40 ms, faster than 20.55% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.

Idea: 直接生成row。
"""
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(rowIndex):
            row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]
        return row

class Solution_3:
"""
Runtime: 40 ms, faster than 20.55% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.
"""
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
        
class Solution_4:
"""
Runtime: 36 ms, faster than 70.02% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.

Idea:
先初始化row，然后更新。
 Init:   [0,0,0,0]
 step_0: [1,0,0,0]
 step_1: [1,1,0,0]
 step_2: [1,2,1,0]
 step_3: [1,3,3,1]
"""
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0]*(rowIndex+1)
        row[0] = 1
        for i in range(rowIndex+1):
            j = i
            while j >= 1:
                row[j] += row[j-1]
                j -= 1
        return row