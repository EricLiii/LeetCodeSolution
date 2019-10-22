class Solution_1:
"""
Author: Zefeng

Runtime: 84 ms, faster than 7.56% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.9 MB, less than 6.25% of Python3 online submissions for Valid Anagram.

slow.
"""
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst1, lst2 = [], []
        for i in range(len(s)):
            lst1.append(s[i])
            lst2.append(t[i])
        lst1.sort()
        lst2.sort()
        return lst1 == lst2
        
class Solution_2:
"""
Runtime: 68 ms, faster than 38.96% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
"""
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
class Solution_3:
"""
Runtime: 64 ms, faster than 50.77% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.1 MB, less than 9.38% of Python3 online submissions for Valid Anagram.
"""
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2