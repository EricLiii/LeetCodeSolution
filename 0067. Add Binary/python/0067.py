class Solution_1:
"""
Runtime: 40 ms, faster than 71.77% of Python3 online submissions for Add Binary.
Memory Usage: 13.7 MB, less than 5.55% of Python3 online submissions for Add Binary.
"""
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        carry=0
        i=len(a)-1
        j=len(b)-1
        while carry or i>=0 or j>=0:
            total=carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            result.append(str(total%2))
            carry=total//2
        return "".join(result[::-1])
        
class Solution_2:
"""
Runtime: 44 ms, faster than 43.28% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Add Binary.

记这个吧!
"""
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        carry = 0
        while a or b or carry: #加一个对carry的检查可以保证11+1=100的情况。
            summ = carry #直接将summ赋为carry，后面就不用再专门加carry了。
            if a:    
                summ += int(a[-1])
            if b:
                summ += int(b[-1])
            carry = summ // 2
            s += str(summ % 2)
            a, b = a[:-1], b[:-1]
        return s[::-1]
