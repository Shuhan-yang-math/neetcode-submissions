class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            a=n &1 
            result=(result<<1)+a
            n=n>>1
        return result
        