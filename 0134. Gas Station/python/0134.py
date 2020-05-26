class Solution_1:
"""
Runtime: 60 ms, faster than 84.71% of Python3 online submissions for Gas Station.
Memory Usage: 14.8 MB, less than 6.25% of Python3 online submissions for Gas Station.

Link: https://www.cnblogs.com/boring09/p/4248482.html

Link: https://blog.csdn.net/qq508618087/article/details/50990076 这个链接讲得比较清楚.
"""
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #这里的total其实是total短缺。
        start, tank, total = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                #这里要注意是i+1, 因为是到不了i的，同时到i为止的短缺也会被计入total，
                #所以要更新start为i+1
                start = i+1 
                #total是start之前欠下的油量,是负值.
                total += tank
                tank = 0
        #if total + tank < 0 判断从最新的start开始计算之后,tank能否填补之前的亏空.
        #如果total + tank >= 0,说明从最新的start开始直到i=len(gas)-1,剩余的gas足够支持从i=0走到start-1.
        #这就说明从start开始走是可行的.
        return -1 if total + tank < 0 else start