class Solution_1:
"""
Runtime: 48 ms, faster than 54.58% of Python3 online submissions for Word Break.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Word Break.

Link: https://cloud.tencent.com/developer/article/1442628

Idea:
贪心算法是错误的，假如输入为"aaaaaaa",["aaa","aaaa"],那么"aaaaaaa"会被分成"aaa","aaa","a".返回False，但正确答案是True.
所以要用DP.
"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #关键是dp的创建和遍历范围的选取.
        #这里dp长度是s的长度加1.
        #dp[0]赋为True.
        dp = [False] * (len(s)+1)
        dp[0] = True
        #i从1开始遍历.
        #j从0开始遍历.
        for i in range(1, len(s)+1):
            for j in range(i):
                #dp[j] = True 说明s中s[:j-1]是可以完全划分为子字符串的.
                #s[j:i]检查以s[j]开头,s[i-1]结尾的子字符串在不在wordDict中.
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
class Solution:
"""
Runtime: 48 ms, faster than 54.30% of Python3 online submissions for Word Break.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Break.

另一种遍历方法，但是思路是一样的.
"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i >= len(word) and dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        return dp[-1]