class Solution_1:
"""
Runtime: 72 ms, faster than 77.72% of Python3 online submissions for Power of Three.
Memory Usage: 14.1 MB, less than 7.41% of Python3 online submissions for Power of Three.

Bad question.
"""
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 is 3^19. 3^20 > int_max.
        return n > 0 and 1162261467 % n == 0