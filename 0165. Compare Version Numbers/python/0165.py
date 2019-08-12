class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 34.76% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Compare Version Numbers.
"""
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1, lst2 = version1.split("."), version2.split(".")
        #先把两个数列补齐，省的之后判断谁长谁短。
        if len(lst1) > len(lst2):
            lst2 += [0]*(len(lst1)-len(lst2))
        else:
            lst1 += [0]*(len(lst2)-len(lst1))
        for i in range(len(lst1)):
            if int(lst1[i]) != int(lst2[i]):
                return -1 if int(lst1[i]) < int(lst2[i]) else 1
        return 0
        
        """
        Link: https://leetcode.com/problems/compare-version-numbers/discuss/50800/2-4-lines-Python-3-different-ways
        链接中的solution2有个小trick: [0]*-2 = [].
        这样只需要一行 v1 + [0]*d, v2 + [0]*-d 就可以将两个列表补齐，不需要像我的方法中那样if...else...
        但是要注意solution2是不能AC的，一是因为v1,v2是两个map的object，需要list()遍历取值;
        二是python3中已经没有cmp函数了。
        """