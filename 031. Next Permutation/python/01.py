class Solution:
"""
Author: Zefeng

Runtime: 36 ms, faster than 96.56% of Python3 online submissions for Next Permutation.
Memory Usage: 13.2 MB, less than 62.44% of Python3 online submissions for Next Permutation.

Actually, runtime varies a lot everytime I submit, from 36ms to 56ms.

Idea:
1. 从末尾开始比较大小，当遇到当前项大于下一项时，记录下一项的正序位置(flag)。若遍历完都未发现flag项，则将整个list逆序排列。
2. 从flag+1项开始正序遍历，比较第j项与flag项。如果第j项小于或等于第flag项，则将flag项与j-1项互换，break。若不存在小于或等于flag项的j项，则将flag项与list最后一项互换。
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