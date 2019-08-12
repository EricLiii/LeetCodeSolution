class Solution_1:
"""
Runtime: 44 ms, faster than 27.26% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.4 MB, less than 8.70% of Python3 online submissions for Reverse Words in a String.
"""
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip(" ")
        stack = []
        tmp = ""
        for i in range(len(s)):
            if s[i] != " ":
                tmp += s[i]
                if i == len(s)-1:
                    stack.append(tmp)
            else:
                #Handle连续空格的情况
                if tmp:
                    stack.append(tmp)
                    tmp = ""
        stack.reverse()
        res = " ".join(stack)
        return res
        
class Solution_2:
"""
Runtime: 36 ms, faster than 75.54% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.4 MB, less than 8.70% of Python3 online submissions for Reverse Words in a String.
"""
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip(" ")
        #这里需要判断连续空格是因为用了split(" ").其实这样是没有意义的。见solution_3.
        lst = s.split(" ")
        #当有连续空格时，split会将空的string""也算作lst的成员，所以需要加if item 做甄别。
        lst = [item for item in lst if item and " " not in item]
        lst.reverse()
        return " ".join(lst)
        
        """
        关于reverse() 和 reversed():
            foo.reverse() actually reverses the elements in the container. 
            reversed() doesn't actually reverse anything, it merely returns an object 
            that can be used to iterate over the container's elements in reverse order. 
            If that's what you need, it's often faster than actually reversing the elements.
            但是reversed()返回的是一个迭代器，需要去遍历才可以得到reverse的数据。
            而reverse()是in-place操作。
        """
        
class Solution_3:
"""
Runtime: 36 ms, faster than 75.54% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.3 MB, less than 8.70% of Python3 online submissions for Reverse Words in a String.
"""
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        #split()会以默认的所有的空字符，包括空格、换行(\n)、制表符(\t)等进行分割。
        #所以不需要strip(" "), 也不需要检查连续空格.
        lst = s.split()
        return " ".join(reversed(lst))