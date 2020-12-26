class Solution:
"""
Runtime: 756 ms, faster than 38.44% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.5 MB, less than 43.27% of Python3 online submissions for Substring with Concatenation of All Words.

https://blog.csdn.net/csdn0006/article/details/107703067

Zefeng
"""
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        result = []
        k = len(words[0])
        le = k * len(words)
        
        w_dict = {}
        for w in words:
            w_dict[w] = w_dict.get(w, 0) + 1
        
        for i in range(len(s)):
            j = i + le
            if j > len(s):
                continue
            w_count = {}
            flag = True
            for p in range(i, j, k):
                if s[p:p+k] not in words:
                    flag = False
                    break
                w_count[s[p:p+k]] = w_count.get(s[p:p+k], 0) + 1
                if w_count[s[p:p+k]] > w_dict[s[p:p+k]]:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result