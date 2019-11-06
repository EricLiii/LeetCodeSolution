class Solution_1:
"""
Runtime: 160 ms, faster than 5.79% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 16.5 MB, less than 5.00% of Python3 online submissions for Isomorphic Strings.

https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
"""
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        #字典中的key是出现过的字符，而value是每个字符出现过的位置.
        #因此只要比较s和t是否在同样的位置出现了同个字符(即在s或t中,这些位置上的字符是一样的)即可.
        #而sorted是为了进行比较(通过values()获得的迭代器的顺序是不定的).
        return sorted(d1.values()) == sorted(d2.values())
        
class Solution_2:
"""
Author: Zefeng

Runtime: 68 ms, faster than 11.73% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 15.4 MB, less than 5.00% of Python3 online submissions for Isomorphic Strings.

思路差不多.
"""
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]].append(i)
            else:
                dic1[s[i]] = [i]
                
            if t[i] in dic2:
                dic2[t[i]].append(i)
            else:
                dic2[t[i]] = [i]
            
            if dic1[s[i]] != dic2[t[i]]:
                return False
        return True