class Solution_1:
"""
Runtime: 168 ms, faster than 93.15% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 16.8 MB, less than 11.11% of Python3 online submissions for Wiggle Sort II.

https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof

用了python的sort，时间复杂度是nlogn.
TODO: 目前没找到用python的O(n)解法,以后找!
"""
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2]) - 1
        # 这里要熟悉slice的用法.当step=-1的时候:
        # if input = [1, 5, 1, 1, 6, 4], then mid = len(nums[::2]) - 1 = 2,
        # nums[:mid:-1] = [4, 6, 1].
        # 即当step=-1时，从后往前找，不包括mid.
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]