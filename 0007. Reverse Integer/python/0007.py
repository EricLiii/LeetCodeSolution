class Solution_1:
"""
#Runtime: 68 ms, faster than 41.81% of Python3 online submissions for Reverse Integer.
#Memory Usage: 13.4 MB, less than 5.71% of Python3 online submissions for Reverse Integer.

Idea:
res是int,思路是给int添加新的个位。
"""
    def reverse(self, x: int) -> int:
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x //= 10
        return res * isPos
        
class Solution_2:
"""
Author: Zefeng

Runtime: 36 ms, faster than 83.92% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 5.40% of Python3 online submissions for Reverse Integer.

Idea:
res是string，思路是弹出x的个位。
"""
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = ""
        if x < 0:
            res += "-"
        x = abs(x)
        while x != 0:
            res += str(x % 10)
            x = x // 10
        res_ = int(res)
        return res_ if res_ >= -pow(2, 31) and res_ <= pow(2, 31)-1 else 0  # OR 2**31
        
class Solution_3:
"""
Runtime: 32 ms, faster than 96.24% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 5.40% of Python3 online submissions for Reverse Integer.

Idea:
将x变为string然后倒序。
"""
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        # 这里有一点需要注意：
        # 此处只判断了r<2**31, 也许你会疑惑假如r==2**31呢？即假如期望结果是-2**31呢？
        # 假设期望结果是-2**31,那么输入应该是-8463847412。但这明显不是一个valid的输入（超出支持范围）。
        # 因此这里只需判断r<2**31.
        return s*r * (r < 2**31)