class Solution_1:
"""
Runtime: 192 ms, faster than 78.74% of Python3 online submissions for Perfect Squares.
Memory Usage: 13.6 MB, less than 70.00% of Python3 online submissions for Perfect Squares.

https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
"""
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt


class Solution_2:
"""
https://leetcode.com/problems/perfect-squares/discuss/71495/An-easy-understanding-DP-solution-in-Java

这是一个好思路，用的是dp。但是源代码是java，换成python会超时。
“”“
"""
