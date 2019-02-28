class Solution:
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
