class Solution:
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
