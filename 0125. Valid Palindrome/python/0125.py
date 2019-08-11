class Solution_1:
"""
Runtime: 60 ms, faster than 50.26% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.3 MB, less than 46.43% of Python3 online submissions for Valid Palindrome.
"""
    def isPalindrome(self, s: str) -> bool:
        if not s: 
            return True
        left, right = 0, len(s)-1
        #第一个要注意的就是left<right OR left<=right?
        #其实left<right 和 left<=right都可以。但是left<right就够了，没必要left<=right。
        while left < right:
            #第二个要注意的就是以下语句是if->elif->elif->else,如果if->if....会出错.
            #python string的isalnum()要会用。
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            #python 将大写转小写，小写转大写要会用。
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
        
class Solution_2:
"""
Runtime: 56 ms, faster than 64.18% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.3 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

Idea:
更简洁。
"""
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]