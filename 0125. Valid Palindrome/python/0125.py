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
        #这个简洁写法（列表解析式）要记住.
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
        
class Solution_3:
"""
Runtime: 224 ms, faster than 5.26% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 21.43% of Python3 online submissions for Valid Palindrome.

思路都是一样的，但是这个solution慢得离谱. 可能是因为 s = s[:i] + s[i+1:].
"""
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        while i < len(s):
            if not s[i].isalpha() and not s[i].isdigit():
                s = s[:i] + s[i+1:]
            else:
                i += 1
        return s == s[::-1]