"""
WRONG:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray=[]
        sum=0
        for i in range(len(nums)):
            if not subarray or (nums[i]>0 or nums[i]==0):
                subarray.append(nums[i])
                sum+=nums[i]
            elif nums[i]>subarray[0]:
                sum=sum+(nums[i]-subarray[0])
                del subarray[0:1]
                subarray.append(nums[i])  
        return sum
"""

class Solution_1:
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max=float('-inf')
        max_ending_here=0
        for num in nums:
            if max_ending_here>0:
                max_ending_here+=num
            else:
                max_ending_here=num
            overall_max=max(overall_max,max_ending_here)
        return overall_max

class Solution_2:
'''
ref: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=933s
'''
# @param A, a list of integers
# @return an integer
# 6:57
def maxSubArray(self, A):
    if not A:
        return 0
    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)#只需要知道到num为止sum最大的子数列的sum是多少，没必要知道具体是哪几个数字；而且不一定要和num连起来。
    return maxSum

