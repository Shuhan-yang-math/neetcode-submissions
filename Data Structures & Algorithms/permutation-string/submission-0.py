class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        d=sorted(s1)
        if n1>n2:
            return False
        for i in range(n2-n1+1):
            x=sorted(s2[i:i+n1])
            if x==d:
                return True
        return False
        