class Solution_1:
"""
Runtime: 60 ms, faster than 88.43% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 25.8 MB, less than 63.33% of Python3 online submissions for Repeated DNA Sequences.
"""
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        container = set()
        res = set()          #这里container和res用set都是为了避免重复存储。
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub not in container:
                container.add(sub)
            else:
                res.add(sub) 
        return res
        
class Solution_2:
"""
Author: Zefeng

Runtime: 72 ms, faster than 64.46% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 27.5 MB, less than 16.67% of Python3 online submissions for Repeated DNA Sequences.

和solution_1一样，只不过是自己做出来的. 但是没有solution_1简洁.
"""
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        dic = {}
        for i in range(len(s) - 10 + 1):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            else:
                dic[s[i:i+10]] += 1
        res = [k for k, v in dic.items() if v >1]
        return res