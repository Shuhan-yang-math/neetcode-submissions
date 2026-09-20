class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A={}
        B={}
        for i in s:
            A[i]=A.get(i,1)+1
        for j in t:
            B[j]=B.get(j,1)+1
        for a in A:
            if a not in B or A[a]!=B[a]:
                return False
        for b in B:
            if b not in A or A[b]!=B[b]:
                return False
        return True

        