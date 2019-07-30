class Solution_1:
"""
Runtime: 112 ms, faster than 71.22% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.4 MB, less than 21.08% of Python3 online submissions for Group Anagrams.
"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            #tuple可以作为dict的key.
            #sorted()是在copy上进行操作，不影响w.
            key = tuple(sorted(w))
            #dict的get()函数：
            #   get(key, value):
            #       1.如果key在字典中，返回对应value;
            #       2.如果key不在字典中而且没有指定value(即value=None),返回None;
            #       3.如果key不在字典中但是指定了value(eg,[]),返回value.
            d[key] = d.get(key, []) + [w]
        return list(d.values()) #这里要用list()，否则返回的是一个dict_values([])的object.