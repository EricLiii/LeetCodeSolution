class Solution:
"""
Runtime: 76 ms, faster than 98.52% of Python3 online submissions for Insert Interval.
Memory Usage: 16.1 MB, less than 8.00% of Python3 online submissions for Insert Interval.

https://blog.csdn.net/qq_29592167/article/details/83273331
"""
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        pos = -1
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                pos = i
                break
	#这里要注意的是如果intervals每一项的第一个元素都小于newInterval的第一个元素的话，newInterval应该是append到intervals.
	#否则可以直接insert到pos位置。
        if pos > -1:
            intervals.insert(pos, newInterval)
        else:
            intervals.append(newInterval)
        res = []
        start, end = intervals[0][0], intervals[0][-1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][-1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][-1]
        res.append([start, end])
        return res
