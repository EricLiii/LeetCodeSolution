class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 60.08% of Python3 online submissions for Add Digits.
Memory Usage: 14.1 MB, less than 5.26% of Python3 online submissions for Add Digits.
"""
    def addDigits(self, num: int) -> int:
        while num//10 > 0:
            summ = 0
            while num:
                a = num % 10
                num //= 10
                summ += a
            num = summ
        return num
        
class Solution_2:
"""
Runtime: 36 ms, faster than 85.45% of Python3 online submissions for Add Digits.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Add Digits.

https://leetcode.com/problems/add-digits/discuss/68580/Accepted-C%2B%2B-O(1)-time-O(1)-space-1-Line-Solution-with-Detail-Explanations
https://blog.csdn.net/will130/article/details/51187597
"""
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9