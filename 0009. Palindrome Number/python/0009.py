class Solution:
"""
Author: Zefeng

Runtime: 96 ms, faster than 12.83% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 5.11% of Python3 online submissions for Palindrome Number.
"""
    def isPalindrome(self, x: int) -> bool:
        lst = []
        tmp = x
        if x < 0:
            return False
        if x == 0:
            return True
        while x:
            lst.append(x%10)
            x = x // 10
        x_ = 0
        while lst:
            x_ = x_*10 + lst.pop(0)
        return True if tmp == x_ else False


class Solution_2:
"""
Runtime: 76 ms, faster than 46.81% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 5.11% of Python3 online submissions for Palindrome Number.
"""
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x%10 == 0):
            return False
        num = 0
        while x > num:
            num = num*10 + x%10
            x = x//10
        #如果是回文：
        #   1.当x位数是偶数的时候, x==num
        #   2.当x位数是奇数的时候, x==num//10
        #如果上述两条件均不满足，则不是回文。
        #本方法不必遍历全部位数，值得学习!
        return x == num or x == num//10 

        

class Solution_3:
"""
Use string.

Trivial.
"""
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False
            
            
