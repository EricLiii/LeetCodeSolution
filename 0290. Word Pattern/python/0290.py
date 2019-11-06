class Solution_1:
"""
Runtime: 32 ms, faster than 89.67% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Pattern.

https://leetcode.com/problems/word-pattern/discuss/73433/Short-in-Python
"""
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        """
        The find() method returns the lowest index of the substring if it is found in given string. 
        If its is not found then it returns -1.
        
        index() is an inbuilt function in Python, which searches for given element from start of the list 
        and returns the lowest index where the element appears.
        
        因此，在经过这两个操作后，相同元素所在位置的数字应该是一样的，均为该元素第一次出现的index.
        
        注意，不能直接判断 map(s.find, s) == map(t.index, t),因为这两个是不同的object，一定不相同。
            需要先变成列表，再判断.
        """
        return [*map(s.find, s)] == [*map(t.index, t)]
        
        
class Solution_2:
"""
Runtime: 36 ms, faster than 68.20% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Pattern.

https://leetcode.com/problems/word-pattern/discuss/73599/Share-my-python-solution-with-two-dictionaries

方法很好，但是细节还需要理解.目前不保证可以靠自己解决这个题.
"""
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(pattern) != len(words):
            return False

		# use two dictionaries, mapping character / string with index
        pattern_map, word_map = {}, {}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            
            pattern_map[pattern[i]] = word_map[words[i]] = i
        return True