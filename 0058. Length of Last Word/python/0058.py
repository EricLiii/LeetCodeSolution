class Solution_1:
"""
Runtime: 36 ms, faster than 67.01% of Python3 online submissions for Length of Last Word.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Length of Last Word.
"""
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        end=-1
        while i>=0:
            if s[i]==' ' and end!=-1:
                return end-i
            if s[i]!=' ' and end ==-1:
                end =i                  # find the first letter from the end of string s.
            i-=1
        return end+1 if end!=-1 else 0  # if end==-1: the string is empty or only consists of spaces.
                                        # if end!=-1: the string s doesn't have any space OR only has spaces at the end.

                                        
class Solution_2:
"""
Author: Zefeng

Runtime: 36 ms, faster than 67.01% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Length of Last Word.

记我这个，上面那个没什么特别的。
"""
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        #越是简单题越要考虑周全，不放过edge case.
        #这里strip()就是避免" sss "
        s = s.strip(" ")
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return len(s[i+1:])
        return len(s)