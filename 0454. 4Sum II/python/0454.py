class Solution_1:
"""
Runtime: 296 ms, faster than 49.64% of Python3 online submissions for 4Sum II.
Memory Usage: 34.5 MB, less than 8.33% of Python3 online submissions for 4Sum II.

https://leetcode.com/problems/4sum-ii/discuss/93927/python-O(n2)-solution-with-hashtable
"""
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashtable = {}
        
        # AB, CD分组的原因是这样的时间复杂度是O(n).
        # ABC, D分组是能做出来的，但是超时.
        for a in A:
            for b in B :
                hashtable[a+b] = hashtable.get(a+b, 0) + 1
                
        count = 0         
        for c in C :
            for d in D :
                if -(c+d) in hashtable :
                    count += hashtable[-(c+d)]
        return count