class Solution_1:
"""
Runtime: 56 ms, faster than 93.42% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for ZigZag Conversion.
"""
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        L = [""] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            #因为当numRows是1的时候，step无论如何都是1.所以开头要考虑这个情况.
            elif index == numRows -1: 
                step = -1
            index += step
        return "".join(L)
