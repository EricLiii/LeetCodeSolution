class Solution_1:
"""
Author: Zefeng

Runtime: 148 ms, faster than 9.96% of Python3 online submissions for Rotate Array.
Memory Usage: 15.3 MB, less than 5.04% of Python3 online submissions for Rotate Array.
"""
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

class Solution_2:
"""
Runtime: 72 ms, faster than 78.96% of Python3 online submissions for Rotate Array.
Memory Usage: 15.1 MB, less than 5.04% of Python3 online submissions for Rotate Array.
"""
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #!!最重要的部分!!: 因为k有可能大于nums的长度，所以要先取余。不然输入以下case时会出错：
        #   input=[1,2], k=3.
        #   Expected: [2,1], but output is [1,2]
        k %= len(nums)
        #对整个list可以用reverse（）
        nums.reverse()
        #如果想仅仅倒序部分list，不能nums[0:k].reverse(),因为nums[0:k]会创建一个复制，改变这个复制的操作不会影响原list。
        #也不能nums[0:k] = nums[0:k].reverse(),具体原因需要看源码，这里先记住。
        nums[0:k] = nums[0:k][::-1]
        nums[k:] = nums[k:][::-1]   

class Solution_3:
"""
Runtime: 72 ms, faster than 78.96% of Python3 online submissions for Rotate Array.
Memory Usage: 15 MB, less than 5.04% of Python3 online submissions for Rotate Array.

Idea:
A little important thing to be cautious:
    nums[:] = nums[n-k:] + nums[:n-k] can't be written as: nums = nums[n-k:] + nums[:n-k] on the OJ.
    The previous one can truly change the value of old nums, 
    but the following one just changes its reference to a new nums not the value of old nums.
"""
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]     
        
class Solution_4:
"""
Runtime: 72 ms, faster than 78.96% of Python3 online submissions for Rotate Array.
Memory Usage: 15.3 MB, less than 5.04% of Python3 online submissions for Rotate Array.

Idea:
Improved solution_3, O(1) space
"""
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] 

        