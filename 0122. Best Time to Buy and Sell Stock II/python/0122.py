class Solution:
"""
Runtime: 104 ms, faster than 6.41% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.8 MB, less than 5.49% of Python3 online submissions for Best Time to Buy and Sell Stock II.

Idea:
这个题主要就是考的一个思想。
现实生活中你其实是不知道明天的价格，但是本题中已经将所有的价格告诉你，如果你想获得最大的利益，只需要当明天的价格高于今天的价格的时候，
在今天买入，在明天抛售即可。
假如后天的价格比明天高，你可以在明天买入，在后天卖出。
虽然题中并未明确说明是否可以当天卖出当天再买入，但是今天买后天卖的结果和今天买明天卖、明天再买后天再卖的结果是一样的(前提是今天、明天和后天的价格是递增的).
"""
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total