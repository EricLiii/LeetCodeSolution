class Solution_1:
"""
Author: Zefeng

Runtime: 40 ms, faster than 26.76% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 5.31% of Python3 online submissions for Plus One.
"""
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        l = len(digits)
        for i in range(l):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == l-1:
                    digits.append(1)
        digits.reverse() 
        #需要注意,reverse()是in-place操作，无返回。
        #一开始我出错就是因为res = digits.reverse()，其实res是None.
        return digits

class Solution_2:
"""
Author: Zefeng

Runtime: 40 ms, faster than 26.76% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 5.40% of Python3 online submissions for Plus One.

Idea:
Improved solution_1, remove reverse() operation.
"""
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in range(l-1, -1, -1):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits


class Solution_3:
"""
Runtime: 40 ms, faster than 26.76% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 5.40% of Python3 online submissions for Plus One.

Idea:
Same with solution_2.
"""
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        forward=True
        while i>=0 and forward==True:
            if digits[i]==9:
                digits[i]=0
            else: 
                digits[i]+=1
                forward=False
            i-=1
        if forward==True:
            digits.insert(0,1)
        return digits

class Solution_4:
"""
Runtime: 40 ms, faster than 26.76% of Python3 online submissions for Plus One.
Memory Usage: 13.7 MB, less than 5.40% of Python3 online submissions for Plus One.

Idea:
Different method.
"""
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        while i>=0 and digits[i]==9:
            digits[i]=0
            i-=1
        if i==-1:
            return [1]+digits
        return digits[:i]+[digits[i]+1]+digits[i+1:]
