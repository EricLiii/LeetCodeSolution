class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.strip()
        neg=False
        if str and str[0] =='-':
            neg=True
        if str and (str[0]=='+' or str[0]=='-'):             
            str=str[1:]
        if not str:
            return 0
        
        digits={i for i in '0123456789'}   # Or use isdigit() instead of dic to check if it is an integer, will be faster
        result=0
        for c in str:
            if c not in digits:
                break
            result=result*10+int(c)
        if neg:
            result=-result
        result=max(min(result,2**31-1),-2**31)
        return result
                
