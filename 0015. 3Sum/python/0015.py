class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
    Runtime: 908 ms, faster than 65.63% of Python3 online submissions for 3Sum.
    Memory Usage: 16.6 MB, less than 89.71% of Python3 online submissions for 3Sum.
    """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    #因为前面已经将nums排序了，而且i, l, r是递增的，所以不需要判读是否已经存在于res中.
                    #记住这个技巧
                    res.append((nums[i], nums[l], nums[r])) #这里添加的是tuple，最后返回的是一个由tuple组成的list，不知道网站为什么最后还是接受了答案。
                    #不过append tuple 确实比append list 快一点。
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    #已经判断过l之后，其实不需要再判断r也可以通过
                    #但是判断一下会加快速度。
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


class Solution:
想一下如何定义一个twoSum函数，并通过调用这个函数来实现目标.
之前试了几次都失败了.