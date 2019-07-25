class Solution_1:
"""
Runtime: 68 ms, faster than 44.87% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.2 MB, less than 19.39% of Python3 online submissions for Maximum Product Subarray.

Link:http://bangbingsyb.blogspot.com/2014/11/leetcode-maximum-product-subarray.html
"""
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sofar = max_p = min_p = nums[0]
        for i in range(1, len(nums)):
            # 这里注意如果没有先用max_p_tmp暂存更新后的最大值，在计算min_p的时候所用的max_p就已经是更新后的值了，
            # 但是我们想用的是更新前的max_p，所以需要有一个tmp.
            max_p_tmp = max(max_p*nums[i], min_p*nums[i], nums[i])
            min_p = min(max_p*nums[i], min_p*nums[i], nums[i])
            max_p = max_p_tmp
            max_sofar = max(max_p, min_p, max_sofar)
        return max_sofar
        
class Solution_2:
"""
Runtime: 64 ms, faster than 71.15% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 13.9 MB, less than 26.87% of Python3 online submissions for Maximum Product Subarray.

Same with solution_1.
"""
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sofar = max_p = min_p = nums[0]
        for i in range(1, len(nums)):
            # 做一个判断，之后就不用再分配一个空间储存tmp了.
            if nums[i] < 0:
                max_p, min_p = min_p, max_p
            max_p = max(max_p*nums[i], nums[i])
            min_p = min(min_p*nums[i], nums[i])
            max_sofar = max(max_p, min_p, max_sofar)
        return max_sofar