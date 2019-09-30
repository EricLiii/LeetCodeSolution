class Solution_1:
"""
Runtime: 32 ms, faster than 89.35% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 13.9 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.

Link:https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
"""
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1) #注意这里长度是n+1，因为有G[0]存在.
        G[0] = G[1] = 1
        for i in range(2, n+1): #从2开始，因为G[0],G[1]已经知道了。
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]
        
class Solution_2:
"""
Link: https://leetcode.com/problems/unique-binary-search-trees/discuss/31826/Python-solutions-(DP-%2B-Catalan-number)

Catalan number,卡特兰数，应用很多，以后抽时间看一下.
"""