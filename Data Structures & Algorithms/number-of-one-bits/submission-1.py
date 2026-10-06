class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            a=n & 1
            count+=a
            n=n>>1
        return count
        