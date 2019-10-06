class Solution_1:
"""
Author: Zefeng

Runtime: 1228 ms, faster than 6.00% of Python3 online submissions for Single Number.
Memory Usage: 16.2 MB, less than 5.06% of Python3 online submissions for Single Number.
"""
    def singleNumber(self, nums: List[int]) -> int:
        lst = []
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                lst.remove(nums[i])
        return lst[0]
        
class Solution_2:
"""
Author: Zefeng

Runtime: 104 ms, faster than 43.18% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 5.06% of Python3 online submissions for Single Number.
"""
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[i]
            if i == len(nums)-1 and nums[i] != nums[i-1]:
                return nums[i]
            if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                return nums[i]
                
                
class Solution_3:
"""
XOR, 同0异1.

Runtime: 100 ms, faster than 67.91% of Python3 online submissions for Single Number.
Memory Usage: 16.2 MB, less than 5.06% of Python3 online submissions for Single Number.

Idea:
利用异或的特性：a^b^b=a. 注意，异或是要变成二进制运算的.
"""
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)): #这里注意，从1开始。
            nums[0] ^= nums[i]
        return nums[0]
        
class Solution_4:
"""
Runtime: 100 ms, faster than 70.52% of Python3 online submissions for Single Number.
Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number.

记solution_3 and 4.
"""
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)