class RandomizedSet_1:
"""
Runtime: 564 ms, faster than 6.14% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 18 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).

https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums:
            return False
        else:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
              
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.nums:
            # 这里的思路就是将self.nums中要被remove的值变为nums[-1]的值，同时在self.pos中做出相应改变.
            # 这样只需要pop出nums的最后一个即可,是O(1)的.如果直接self.nums.pop(idx)不是O(1).
            # 同时由于之前在-1位置的值已经被复制到idx处,故得以保留.
            idx, last = self.pos[val], self.nums[-1]
            self.pos[last] = idx
            self.nums[idx] = last
            del self.pos[val]
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]
        
class RandomizedSet:
"""
Runtime: 96 ms, faster than 86.99% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 17.8 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).

https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos: #这里用self.pos而不是self.nums所以比solution_1更快，因为list是O(n), dict是O(1).
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.pos[last] = idx
            self.nums[idx] = last
            del self.pos[val]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]