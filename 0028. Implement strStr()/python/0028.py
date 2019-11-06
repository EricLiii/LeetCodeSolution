class Solution_1:
"""
Runtime: 56 ms, faster than 13.77% of Python3 online submissions for Implement strStr().
Memory Usage: 14.1 MB, less than 12.31% of Python3 online submissions for Implement strStr().
"""
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            for j in range(len(needle)):
                #先判断是否超出范围，再判断是否相等。
                #if i + len(needle) > len(haystack) 而不是 if i + len(needle) >= len(haystack).
                if i + len(needle) > len(haystack):
                    break
                #这里是haystack[i+j],不是haystack[i].
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1
        
class Solution_2:
"""
Runtime: 40 ms, faster than 57.04% of Python3 online submissions for Implement strStr().
Memory Usage: 13.9 MB, less than 12.31% of Python3 online submissions for Implement strStr().

这个更简单，但是似乎不是出题人想要的答案。
不过用在工程上是最好的。
"""
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1