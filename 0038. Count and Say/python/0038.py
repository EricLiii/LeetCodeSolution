class Solution_1:
"""
Runtime: 36 ms, faster than 93.19% of Python3 online submissions for Count and Say.
Memory Usage: 14 MB, less than 6.38% of Python3 online submissions for Count and Say.

Idea: 
Iterate through the previous sequence, when we see a different number, append [1,num] to the new sequence.
When we see the same number, increase its count.
"""
    def countAndSay(self, n: int) -> str:
        sequence = [1]
        for _ in range(n-1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1,num]
                else:
                    next[-2] += 1
            sequence = next
        #将int变为str.
        #记住map在这里的用法.
        return "".join(map(str, sequence))
    
