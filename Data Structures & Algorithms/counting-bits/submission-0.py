class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1(n):
            a=0
            while n>0:
                b=n &1
                a+=b
                n=n>>1
            return a
        A=[]
        for i in range(n+1):
            A.append(count1(i))
        return A
        