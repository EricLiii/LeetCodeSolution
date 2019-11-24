class Solution:
"""
Runtime: 104 ms, faster than 84.44% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 13.3 MB, less than 61.11% of Python3 online submissions for Minimum Window Substring.

https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
"""
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            #在collections.Counter中，如果不存在char,need[char]-=1会使need[char]为负数。
            need[char] -= 1 
            if missing == 0:                     #match all chars
                # need[s[i]] < 0 说明不是t中的char.
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                #将window中第一个在t中的char拿掉，看看后面是否还会出现此char.
                #如果出现，再比较两个window的长短.
                i += 1                           #update i to start+1 for next window
        return s[start:end]