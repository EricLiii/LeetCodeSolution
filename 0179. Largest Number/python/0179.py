import functools 

class Solution:
"""
Runtime: 48 ms, faster than 60.57% of Python3 online submissions for Largest Number.
Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Largest Number.

Link: https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines
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