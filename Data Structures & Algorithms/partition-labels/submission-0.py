class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        A={}
        n=len(s)
        for i in range(n):
            if s[i] not in A:
                A[s[i]]=i
            else:
                A[s[i]]=i
        end=A[s[0]]
        right=A[s[0]]
        B=[]
        j=0
        for i in range(n):
            end=max(end,A[s[i]])
            j=j+1
            if i==end:
                B.append(j)
                j=0
        return B


        