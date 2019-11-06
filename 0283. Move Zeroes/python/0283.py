class Solution_1:
"""
Runtime: 52 ms, faster than 96.34% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes.

https://leetcode.com/problems/move-zeroes/discuss/72011/Simple-O(N)-Java-Solution-Using-Insert-Index

这个方法要记，经常遇见!
"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
            
class Solution_2:
"""
Runtime: 56 ms, faster than 85.85% of Python3 online submissions for Move Zeroes.
Memory Usage: 15 MB, less than 5.97% of Python3 online submissions for Move Zeroes.

https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.
跟solution_1相比，省去了后面全部置0的操作.
"""
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1