class Bad_Solution:
"""
Input:
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

超时
"""
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        self.helper(s, [], wordDict)
        return self.res
        
    def helper(self, s, path, wordDict):
        if not s:
            self.res.append(" ".join(path))
            return
            
        #for i in range(len(s)):
        i = 0
        for w in wordDict:
            if i+len(w)-1 <= len(s) and s[i:i+len(w)] == w:
                self.helper(s[i+len(w):], path+[w], wordDict)



class Solution:
"""
Runtime: 44 ms, faster than 54.06% of Python3 online submissions for Word Break II.
Memory Usage: 14.5 MB, less than 65.16% of Python3 online submissions for Word Break II.

https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
"""
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        # 这道题主要就是容易超时
        # 所以需要利用memo
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res