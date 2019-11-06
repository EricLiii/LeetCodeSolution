import functools 

class Solution_1:
"""
Runtime: 48 ms, faster than 60.57% of Python3 online submissions for Largest Number.
Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Largest Number.

Link: https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines


还是没太懂key的用法，以后有时间再看看.https://juejin.im/post/5a3b7ba06fb9a045104aa988
"""
    def largestNumber(self, nums):
        """
         相当于 if a+b > b+a:
                    return 1
                else:
                    if a+b < b+a:
                        return -1
                    else:
                        return 0
        """
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(_nums)))
        
class Solution_2:
"""
Runtime: 44 ms, faster than 82.72% of Python3 online submissions for Largest Number.
Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for Largest Number.

改成这样就不用reverse了.
"""
    def largestNumber(self, nums: List[int]) -> str:
        compare = lambda a, b: -1 if a+b > b+a else 1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key=functools.cmp_to_key(compare))
        return str(int(''.join(_nums)))
        
        
class Solution_3:
"""
https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).

TODO: 好好看看这个link,借此机会熟悉所有排序方法.
"""