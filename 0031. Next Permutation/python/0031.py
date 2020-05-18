class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 96.56% of Python3 online submissions for Next Permutation.
Memory Usage: 13.2 MB, less than 62.44% of Python3 online submissions for Next Permutation.

Actually, runtime varies a lot everytime I submit, from 36ms to 56ms.

这道题主要就是记思路.

Idea:
1. 从末尾开始比较大小，当遇到当前项大于下一项时，记录下一项的正序位置(flag)。注意，这里flag+1之后的项都是小于flag+1项的，且是递减的。若遍历完都未发现flag项，则将整个list逆序排列。
2. 从flag+1项开始正序遍历，比较第j项与flag项。如果第j项小于或等于第flag项，则将flag项与j-1项互换，break。若不存在小于或等于flag项的j项，则将flag项与list最后一项互换。
值得注意的
3. 此时将nums从flag+1项开始倒序排列，break。
"""
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        for i in range(1, le):
            if nums[-i] <= nums[-i-1]:
                if -i > -(le-1):
                    continue
                else:
                    nums.reverse()
            else:
                flag = le-i-1
                for j in range(flag+1, le):
                    if nums[flag] == nums[j] or nums[flag] > nums[j]:
                        nums[flag], nums[j-1]= nums[j-1], nums[flag]
                        break
                    if j == le-1:
                        nums[flag], nums[-1] = nums[-1], nums[flag]
                nums[flag+1:] = nums[flag+1:][::-1] #这个reverse part of list的方法值得学习。
                break
                
                
class Solution:
"""
Runtime: 44 ms, faster than 42.39% of Python3 online submissions for Next Permutation.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Next Permutation.

基于solution_1的修改,加了一下解释。

"""
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= nums[i-1]:
                continue
            else:
                flag = i-1
                break
        if flag == -1:
            # 注意: nums.reverse()是inplace的，因此可以直接nums.reverse()
            #       而[::-1]不是inplace，所以要有左边，且必须加[:]，否则不是在原地址修改.
            nums[:] = nums[::-1] 
            return
        
        pos = -1
        for j in range(flag+1, len(nums)):
            if nums[j] > nums[flag]:
                continue
            else:
            # 有可能出现相等的情况，例：[1,5,1]下一个是[5,1,1]
                pos = j-1
                break
        if pos == -1:
            nums[flag], nums[-1] = nums[-1], nums[flag]
        else:
            nums[flag], nums[pos] = nums[pos], nums[flag]
        nums[flag+1:] = nums[flag+1:][::-1]