class Solution_1:
"""
Runtime: 96 ms, faster than 58.05% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Palindrome Partitioning.
"""
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path+[s[:i]], res)
                
class Solution_2:
"""
Can find an iterative solution?
"""