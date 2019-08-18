class Solution_1:
"""
Runtime: 36 ms, faster than 87.83% of Python3 online submissions for Gray Code.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Gray Code.

Link: https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)

这是gray code的一个公式.
"""
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results
        
class Solution_2:
"""
想一想不用公式怎么做?
"""