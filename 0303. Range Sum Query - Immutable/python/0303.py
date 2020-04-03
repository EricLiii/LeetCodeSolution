class NumArray:
"""
Runtime: 80 ms, faster than 86.98% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.
"""
    def __init__(self, nums: List[int]):
        self.nums = [0] + nums 
        for i in range(2, len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1] - self.nums[i]
