class BadSolution:
"""
Might be right, but Time Limit Exceeded.
"""
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    diff = prices[j] - prices[i]
                    res = max(res, diff)
        return res
        
class Solution_1:
"""
Also Kadane's Algorithm. Refer to 0053. Maximum Subarray.

Runtime: 80 ms, faster than 26.71% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.8 MB, less than 5.18% of Python3 online submissions for Best Time to Buy and Sell Stock.

Idea:
    A more clear explanation on why sum of subarray works.:
    Suppose we have original array:
    [a0, a1, a2, a3, a4, a5, a6]
    what we are given here(or we calculate ourselves) is:
    [b0, b1, b2, b3, b4, b5, b6]
    where,
    b[i] = 0, when i == 0
    b[i] = a[i] - a[i - 1], when i != 0
    suppose if a2 and a6 are the points that give us the max difference (a2 < a6)
    then in our given array, we need to find the sum of sub array from b3 to b6.

    b3 = a3 - a2
    b4 = a4 - a3
    b5 = a5 - a4
    b6 = a6 - a5

    adding all these, all the middle terms will cancel out except two
    i.e.
    b3 + b4 + b5 + b6 = a6 - a2
    a6 - a2 is the required solution.
    so we need to find the largest sub array sum to get the most profit
    
    其实就是将原数列[a0,....,a6]转化为新数列[b0,....,b6],求这个新数列的Maximum Subarray.
    
    
    
Link: https://www.cnblogs.com/coderJiebao/p/Algorithmofnotes27.html
这个链接讲的时最大子数列之和，解释得比较清楚.
"""
    def maxProfit(self, prices: List[int]) -> int:
        max_curr, max_sofar = 0, 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            #这里也不一定非要与0作比较
            #max_curr = max(diff, max_curr + diff) 也是可以的.
            max_curr = max(0, max_curr + diff)
            max_sofar = max(max_curr, max_sofar)
        return max_sofar