class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or '0' in digits or '1' in digits:
            return []
        
        dic={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
        results=[[]]
        for digit in digits:
            temp=[]
            for result in results:
                for letter in dic[digit]:
                    temp.append(result+[letter])
            results=temp
        return [''.join(result) for result in results]
