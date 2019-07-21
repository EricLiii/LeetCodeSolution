class Solution_1:
"""
Runtime: 44 ms, faster than 16.62% of Python3 online submissions for Sort Colors.
Memory Usage: 13.8 MB, less than 5.23% of Python3 online submissions for Sort Colors.

Idea:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, 
then overwrite array with total number of 0's, 
then 1's and followed by 2's.
"""
    def sortColors(self, nums: List[int]) -> None:
        n_zero, n_one, n_two = 0, 0, 0
        for item in nums:
            if item == 0:
                n_zero += 1
            elif item == 1:
                n_one += 1
            else:
                n_two += 1
        nums[0:n_zero] = [0]*n_zero
        nums[n_zero:n_zero+n_one] = [1]*n_one
        nums[n_zero+n_one:n_zero+n_one+n_two] = [2]*n_two
        
class Solution_2:
"""
Author: Zefeng

Runtime: 36 ms, faster than 75.96% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 5.23% of Python3 online submissions for Sort Colors.

Idea:
遇到0就放到数列开头，遇到2就放到数列末尾，遇到1什么也不做。
"""
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        count = 0
        cur = 0
        while count < l:
            if nums[cur] == 0:
                nums.insert(0, nums.pop(cur))
                cur += 1
            elif nums[cur] == 2:
                nums.append(nums.pop(cur))
            else:
                cur += 1
            count += 1
            
class Solution_3:
"""
Runtime: 36 ms, faster than 75.96% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 5.23% of Python3 online submissions for Sort Colors.

Idea:
Actually, this is the famous Dutch National Flag Problem.
Link: https://www.cnblogs.com/gnuhpc/archive/2012/12/21/2828166.html
"""
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, cur, end = 0, 0, len(nums)-1

        while cur <= end:
            if nums[cur] == 0:
                nums[start], nums[cur] = nums[cur], nums[start]
                cur += 1
                start += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[end] = nums[end], nums[cur]
                end -= 1