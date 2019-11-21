class Solution:
"""
Runtime: 32 ms, faster than 96.28% of Python3 online submissions for First Missing Positive.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time
https://blog.csdn.net/zhc_24/article/details/80363035

"""
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
		#注意这里交换的顺序不能变。
		#如果是 nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]会超时。
		#这是因为if you alter the value of nums[i] first, then ( nums[i] - 1 ) changes. So you must alter nums[nums[i] - 1] first !
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(0, n):
            if nums[i] != i+1:
                return i+1
            
        return n+1
