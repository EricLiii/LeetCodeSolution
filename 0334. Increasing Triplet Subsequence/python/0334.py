class Solution_1:
"""
Runtime: 60 ms, faster than 30.51% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 14.6 MB, less than 11.11% of Python3 online submissions for Increasing Triplet Subsequence.

https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
"""
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False