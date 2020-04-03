class Solution:
"""
Runtime: 36 ms, faster than 90.99% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms
"""
    def maxProfit(self, prices: List[int]) -> int:
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)
