class Solution_1:
"""
Runtime: 1100 ms, faster than 82.65% of Python3 online submissions for Coin Change.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Coin Change.

https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution

这道题重点就是要维护一个visited来检查这个值是否已经出现过。如果出现过就没必要再放入stack中。
如果没有visited，则会超时.
"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        stack = [amount]
        visited = [False] * (amount+1)
        visited[0] = True
        length = 0
        
        while stack:
            tmp = []
            for i in range(len(stack)):
                for j in range(len(coins)):
                    if stack[i] == coins[j]:
                        return length + 1
                    elif stack[i] < coins[j]:
                        continue
                    elif not visited[stack[i]-coins[j]]:
                        tmp.append(stack[i]-coins[j])
                        visited[stack[i]-coins[j]] = True
            stack = tmp
            length += 1 
        return -1
        
class Solution_2:
"""
Runtime: 1640 ms, faster than 33.96% of Python3 online submissions for Coin Change.
Memory Usage: 13.9 MB, less than 30.56% of Python3 online submissions for Coin Change.

https://leetcode.com/problems/coin-change/discuss/77360/C%2B%2B-O(n*amount)-time-O(amount)-space-DP-solution

dp, 这个好记点.
"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
                    
        return -1 if dp[amount] > amount else dp[amount]
