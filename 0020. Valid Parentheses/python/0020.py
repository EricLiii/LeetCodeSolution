class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 46.28% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
"""
    def isValid(self, s: str) -> bool:
        dic = {"(":")","{":"}","[":"]"}
        stack = []
        for item in s:
            if item in dic:
                stack.append(dic[item])
            else:
                if stack and item == stack.pop():
                    continue
                else:
                    return False
        return True if not stack else False 

class Solution_2:
"""
Runtime: 36 ms, faster than 77.72% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.

Idea:
和solution_1思路一致，但是更加简洁。
"""
    def isValid(self, s: str) -> bool:
        stack=[]
        match={'(':')', '[':']', '{':'}'}
        for c in s:
            if c in match:      #if c is one of the key
                stack.append(c)
            else:
                if not stack or match[stack.pop()]!=c:
                    return False
        return not stack
        
        
class Solution:
    def isValid(self, s: str) -> bool:    
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
