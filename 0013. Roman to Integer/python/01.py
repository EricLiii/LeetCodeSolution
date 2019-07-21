class Solution:
  '''
  This is a very slow solution.
  '''
    def romanToInt(self, s: str) -> int:
        mapping={1000:'M',
                  900:'CM',
                  500:'D',
                  400:'CD',
                  100:'C',
                  90:'XC',
                  50:'L',
                  40:'XL',
                  10:'X',
                  9:'IX',
                  5:'V',
                  4:'IV',
                  1:'I'}
        num=0
        i=0
        while i<len(s):
            if i<len(s)-1:
                if s[i:i+2] in mapping.values():
                    num+=list(mapping.keys())[list(mapping.values()).index(s[i:i+2])]
                    i+=2
                else:
                    num+=list(mapping.keys())[list(mapping.values()).index(s[i])]
                    i+=1
            else:
                num+=list(mapping.keys())[list(mapping.values()).index(s[i])]
                i+=1
        return num
       
class Solution:
    '''
    This one is faster because exchange the keys and values
    '''
    def romanToInt(self, s: str) -> int:
        mapping={ 'M':1000,
                'CM':900,
                'D':500,
                'CD':400,
                'C':100,
                'XC':90,
                'L':50,
                'XL':40,
                'X':10,
                'IX':9,
                'V':5,
                'IV':4,
                'I':1}
        num=0
        i=0
        while i<len(s):
            if i<len(s)-1 and s[i:i+2] in mapping:
                num+=mapping[s[i:i+2]]
                i+=2
            else:
                num+=mapping[s[i]]
                i+=1
        return num
