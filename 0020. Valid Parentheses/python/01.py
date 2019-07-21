class Solution:
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
