class Solution_1:
"""
Runtime: 36 ms, faster than 74.09% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.

Idea:
迭代.
"""
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or '0' in digits or '1' in digits:
            return []
        
        dic={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
        results=[[]]
        for digit in digits:
            temp=[]
            for result in results:
                for letter in dic[digit]:
                    temp.append(result+[letter])
            results=temp
        return [''.join(result) for result in results]
        
class Solution_2:
"""
Runtime: 36 ms, faster than 74.09% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.

Idea:
递归.
"""
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[1:])
        additional = mapping[digits[0]]
        #注意c,s相加的顺序。
        #因为前面每次弹出的是第一个字符，所以这里是c+s.
        #若每次弹出的是最后一个字符，则s+c.
        #Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
        return [c + s for s in prev for c in additional]
        
class Solution_3:
"""
Author: Zefeng

Runtime: 36 ms, faster than 73.89% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        for i in range(len(digits)):
            if digits[i] in dic: 
                tmp = []
                chars = dic[digits[i]]
                for char in chars:
                    if not res:
                        tmp.append(char)
                    else:
                        for item in res[-1]:
                            tmp.append(item + char)
                res.append(tmp)
        return res[-1]
