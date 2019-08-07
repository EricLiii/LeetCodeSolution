class Solution_1:
"""
Runtime: 28 ms, faster than 96.55% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Excel Sheet Column Title.

Idea:
https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
"""
    def convertToTitle(self, n: int) -> str:
        """
        dic = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E",
               5:"F", 6:"G", 7:"H", 8:"I", 9:"J",
               10:"K", 11:"L", 12:"M", 13:"N", 14:"O",
               15:"P", 16:"Q", 17:"R", 18:"S", 19:"T",
               20:"U", 21:"V", 22:"W", 23:"X", 24:"Y",
               25:"Z"}
        """
        #记住这个生成list的方法。 尤其是chr()和ord()的用法。
        #[*range(ord('A'), ord('Z')+1)]生成的是：
        #   [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
        dic = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = ""
        while n > 0:
            #这道题的关键就是不要用n%26而是用(n-1)%26,这样保证输入为26的倍数时不会出错。
            #假设输入为26, 26%26=0, 26//26=1,期望输出是Z，但是实际输出是AZ.
            r = (n-1)%26
            res += dic[r]
            n = (n-1) // 26
        return res[::-1]