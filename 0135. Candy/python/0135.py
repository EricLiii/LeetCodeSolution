class Bad_Solution:
"""
可能是对的，但是超时

Zefeng
"""
    def candy(self, ratings: List[int]) -> int:
        lst = [1] * len(ratings)
        for i in range(len(ratings)):
            j = 1
            left, right = 0, 0
            while i+j < len(ratings) and ratings[i+j] < ratings[i+j-1]:
                right += 1
                j += 1
            j = 1
            while i-j >= 0 and ratings[i-j] < ratings[i-j+1]:
                left += 1
                j += 1
            lst[i] = lst[i] + max(left, right)
        return sum(lst)
        
   
class Solution_1:
"""
Runtime: 156 ms, faster than 82.36% of Python3 online submissions for Candy.
Memory Usage: 16.7 MB, less than 46.25% of Python3 online submissions for Candy.

https://leetcode.com/problems/candy/discuss/42769/A-simple-solution
"""
    def candy(self, ratings: List[int]) -> int:
        lst = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                lst[i] = lst[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                lst[i] = max(lst[i], lst[i+1] + 1)
        return sum(lst)