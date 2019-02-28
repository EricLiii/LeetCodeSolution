class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            i=len(s)-1
        end=-1
        while i>=0:
            if s[i]==' ' and end!=-1:
                return end-i
            if s[i]!=' ' and end ==-1:
                end =i
            i-=1
        return end+1 if end!=-1 else 0
