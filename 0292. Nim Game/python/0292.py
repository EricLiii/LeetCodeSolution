class Solution_1:
"""
Author: Zefeng

Runtime: 32 ms, faster than 88.94% of Python3 online submissions for Nim Game.
Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions for Nim Game.
"""
    def canWinNim(self, n: int) -> bool:
        if n == 1 or (n-1) % 4 < 3:
            return True
        else:
            return False
            
class Solution_2:
"""
Runtime: 40 ms, faster than 26.38% of Python3 online submissions for Nim Game.
Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for Nim Game.

https://leetcode.com/problems/nim-game/discuss/73749/Theorem%3A-all-4s-shall-be-false
更简单!
"""
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0