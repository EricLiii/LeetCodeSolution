class Solution_1:
"""
Runtime: 324 ms, faster than 61.78% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19 MB, less than 100.00% of Python3 online submissions for Shuffle an Array.

https://leetcode.com/problems/shuffle-an-array/discuss/85957/easy-python-solution-based-on-generating-random-index-and-swapping
"""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = self.nums[:] #注意这里要用[:]进行deepcopy,若ans=self.nums是引用，会改变self.nums.
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans