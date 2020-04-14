class Solution:
"""
Zefeng

Runtime: 36 ms, faster than 93.08% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.9 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.
"""
    def fizzBuzz(self, n: int) -> List[str]:
        nums = [i for i in range(1, n+1)]
        res = []
        for n in nums:
            if n % 3 == 0 and n % 5 == 0:
                res.append('FizzBuzz')
            elif n % 3 == 0:
                res.append('Fizz')
            elif n % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(n))
        return res