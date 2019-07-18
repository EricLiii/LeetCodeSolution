class Solution:
"""
Author: Zefeng

Just for practice

Runtime: 204 ms, faster than 5.42% of Python3 online submissions for Merge Intervals.
Memory Usage: 24.4 MB, less than 5.09% of Python3 online submissions for Merge Intervals.

Idea:
A simple approach is to start from the first interval and compare it with all other intervals for overlapping, if it overlaps with any other interval, then remove the other interval from list and merge the other into the first interval. Repeat the same steps for remaining intervals after first. This approach cannot be implemented in better than O(n^2) time.
"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= intervals[i][0]:
                    if intervals[j][1] >= intervals[i][0]:
                        intervals[i][0] = intervals[j][0]
                        intervals[i][1] = max(intervals[j][1], intervals[i][1])
                        intervals.pop(j)
                        return self.merge(intervals)
                if intervals[j][0] > intervals[i][0] and intervals[j][0] <= intervals[i][1]:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    intervals.pop(j)
                    return self.merge(intervals)  
        return intervals



class Solution:
"""
Runtime: 44 ms, faster than 92.56% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.1 MB, less than 96.17% of Python3 online submissions for Merge Intervals.

Idea:
Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.
"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        # learn how to sort list with a key argument!
        # 'element' means the elements in intervals list.
        for item in sorted(intervals, key = lambda element: element[0]):
            if out and item[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], item[1])
            else:
                out += item,
        return out