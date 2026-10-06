class Solution:
    def isHappy(self, n: int) -> bool:
        A=set()
        while n!=1:
            a=0
            n1=str(n)
            for i in n1:
                a=a+int(i)*int(i)
            n=a
            if n in A:
                return False
            else:
                A.add(n)
        return True
                
        