class Solution_1:
"""
记这个.
"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        #这里很巧妙，利用了sort()给字符串列表排序的特性:
        #    sort()在给字符串列表排序时，key不是len,而是每个对应位置字符的ascii码。
        #    例如['z', '12', '3', 'a'].sort() -> ['12', '3', 'a', 'z'].
        
        #    https://leetcode.com/problems/longest-common-prefix/discuss/172553/beat-100-python-submission-short-and-clean
        
        #也可以直接比较min(strs)和max(strs).
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
        
class Solution_2:
"""
Runtime: 36 ms, faster than 90.76% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        #关键就是min with key的用法。
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
        
class Solution_3:
"""
Runtime: 40 ms, faster than 71.39% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            #关键是set().
            #set()会将重复的部分剔除。
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        #学会用for...else...
        else:
            return min(strs)
