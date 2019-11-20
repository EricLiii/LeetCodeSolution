class Solution_1:
"""
Runtime: 84 ms, faster than 38.90% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 15.1 MB, less than 17.86% of Python3 online submissions for Find the Duplicate Number.

https://www.cnblogs.com/grandyang/p/4843654.html
"""
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return r

class Solution_2:
"""
Runtime: 68 ms, faster than 97.63% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 15.1 MB, less than 21.43% of Python3 online submissions for Find the Duplicate Number.

https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.

这道题给的nums的性质很特殊，所以可以用这个方法。
nums有n+1个数，分别是1到n和一个重复数字.
我们将每一个位置的数字看成这个位置的下个位置的索引(类似于node.next)。因为nums的特殊之处，这样的假设是一定成立的。即某个位置的数字的索引一定存在，且1到n指向的是不同的位置。
只有重复的两个数字指向同一位置。
这样，nums就成了一个有闭环的链表。
"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
