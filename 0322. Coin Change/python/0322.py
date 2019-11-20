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
