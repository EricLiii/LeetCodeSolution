class Solution_1:
"""
Runtime: 44 ms, faster than 78.03% of Python3 online submissions for Jump Game.
Memory Usage: 14.6 MB, less than 51.14% of Python3 online submissions for Jump Game.

Idea:
由于这个题目只是让我们返回true或者false，其实只要我们找到题目条件的必要条件就行了，把问题转化为判断必要条件是否成立。
其实这道题换种思路就非常容易理解。
从现在的位置 cur_index 到现在位置对应的可以跳跃位置的最大值 jump_max 之和所得到的 next_index 之间
的所有位置，从现在的位置都是 cur_index 都是跳到的。
所以我们可以记录一个最右端的值 right_max, 然后在数组循环过程当中进行 right_max 的更新，只要最后 right_max > nums.size() - 1
我们就可以返回 true。
"""
    def canJump(self, nums: List[int]) -> bool:
        max_right = 0
        for i in range(len(nums)):
            if max_right < i: #这一行不能少，是关键.
                break
            max_right = max(nums[i]+i, max_right)
        return max_right >= len(nums)-1
        
class BadSolution:
"""
Author: Zefeng

Memory Limit Exceeded.
"""
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        return self.dfs(nums)
    
    def dfs(self, nums):
        for i in range(len(nums)):
            if  i == len(nums)-1 and nums[i] >= i:
                return True
            if  i > 0 and nums[i] >= i:
                return self.dfs(nums[i:])
        return False
        
class Solution_2:
"""
Runtime: 36 ms, faster than 97.55% of Python3 online submissions for Jump Game.
Memory Usage: 14.5 MB, less than 67.05% of Python3 online submissions for Jump Game.

Idea: 
Idea is to work backwards from the last index. Keep track of the smallest index that can "jump" to the last index. Check whether the current index can jump to this smallest index.
"""
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-2, -1,-1): #eg, range(4,-2,-1)的范围是4,3,2,1,0,-1.
            if nums[i]+i >= last:
                last = i
        return last <= 0
        
class Solution_3:
"""
Author: Zefeng

Runtime: 44 ms, faster than 78.03% of Python3 online submissions for Jump Game.
Memory Usage: 14.2 MB, less than 99.79% of Python3 online submissions for Jump Game.

Idea:
这个是我最初的想法，先将nums逆序排列，再进行处理，其实本质跟Solution_2的思想是一致的。但是由于编程水平有限，没实现，只得到一个超时的答案，即BadSolution。
"""
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        last = 0
        for i in range(len(nums)):
            if  i > 0 and nums[i] >= i-last:
                last = i
        return last >= len(nums)-1