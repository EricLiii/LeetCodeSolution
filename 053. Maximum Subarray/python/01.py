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

class Solution:
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
'''
ref: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=933s
'''
