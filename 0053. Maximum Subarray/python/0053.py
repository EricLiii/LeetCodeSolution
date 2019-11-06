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
"""
Kadane’s Algorithm

Runtime: 36 ms, faster than 96.78% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 76.79% of Python3 online submissions for Maximum Subarray.
"""
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = float('-inf')
        max_ending_here = 0
        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num #因为如果max_ending_here<0,它和num相加必定小于num，
            overall_max = max(overall_max, max_ending_here)
        return overall_max

class Solution_2:
"""
ref: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=933s

Kadane’s Algorithm

Runtime: 44 ms, faster than 67.62% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.7 MB, less than 42.67% of Python3 online submissions for Maximum Subarray.
"""
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)#只需要知道到num为止sum最大的子数列的sum是多少，没必要知道具体是哪几个数字；而且不一定要和num连起来。
        return maxSum
    
    
class Solution_3:
"""
直接在list内进行处理。

??有疑惑??

Runtime: 40 ms, faster than 88.22% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.9 MB, less than 18.98% of Python3 online submissions for Maximum Subarray.
"""
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
                #本质上还是Kadane’s Algorithm，但是直接在list里进行处理，不需要分配其他空间。
                #这个思路值得学习!
                #但是为什么实际内存使用反而多于solution_1呢？？？？？？
                if nums[i-1] > 0: 
                    nums[i] += nums[i-1]
        return max(nums)
        
        
class Solution_4:
"""
Divide and Conquer algorithm
Link: https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/

Runtime: 124 ms, faster than 5.02% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 64.01% of Python3 online submissions for Maximum Subarray.
"""
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArraySum(nums, 0, len(nums)-1)
        
    def maxSubArraySum(self, arr, l, h) : 
        if (l == h) : 
            return arr[l] 
        m = (l + h) // 2
        return max(self.maxSubArraySum(arr, l, m), 
                   self.maxSubArraySum(arr, m+1, h), 
                   self.maxCrossingSum(arr, l, m, h)) 
    
    def maxCrossingSum(self, arr, l, m, h) : 
        sm = 0; left_sum = float("-inf")

        for i in range(m, l-1, -1) : 
            sm = sm + arr[i] 

            if (sm > left_sum) : 
                left_sum = sm 

        sm = 0; right_sum = float("-inf")
        for i in range(m + 1, h + 1) : 
            sm = sm + arr[i] 

            if (sm > right_sum) : 
                right_sum = sm 

        return left_sum + right_sum; 

