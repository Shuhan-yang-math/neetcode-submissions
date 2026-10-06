class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        a=1
        while n>0:
            if n%2==1:
                a=a*x
            x=x*x
            n=n//2
        return a
        