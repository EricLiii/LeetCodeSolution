class Solution_1:
"""
Runtime: 60 ms, faster than 84.71% of Python3 online submissions for Gas Station.
Memory Usage: 14.8 MB, less than 6.25% of Python3 online submissions for Gas Station.

Link: https://www.cnblogs.com/boring09/p/4248482.html
"""
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, tank, total = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                #total是从i=0开始的油量积累，可能为正，可能为负.
                total += tank
                tank = 0
        return -1 if total+tank<0 else start