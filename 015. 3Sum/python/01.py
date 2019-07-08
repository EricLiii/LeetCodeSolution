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
                    res.append((nums[i], nums[l], nums[r])) #这里添加的是tuple，最后返回的是一个由tuple组成的list，不知道网站为什么最后还是接受了答案。
                    #不过append tuple 确实比append list 快一点。
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
