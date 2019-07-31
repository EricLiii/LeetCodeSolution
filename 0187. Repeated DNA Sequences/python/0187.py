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