class Solution:
"""
Runtime: 1352 ms, faster than 31.47% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 27.8 MB, less than 91.19% of Python3 online submissions for Best Time to Buy and Sell Stock III.

https://www.youtube.com/watch?v=Pw6lrYANjz4

值得看！
"""
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            maxx = float("-inf")
            for i in range(1, len(prices)):
                maxx = max(maxx, -prices[i-1] + dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i] + maxx)
                
        return dp[-1][-1]