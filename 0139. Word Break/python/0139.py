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
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]