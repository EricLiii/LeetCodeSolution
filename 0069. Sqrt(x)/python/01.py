class Solution:
    """
    This is Newton Iteraton method.
    """
    def mySqrt(self, x: int) -> int:
        if (x==0):
            return 0
        guess=x/2
        goon=True
        while goon:
            avg=(guess+x/guess)/2
            if (avg//1==guess//1):
                goon=False
            else:
                guess=avg
        return int(guess//1)
