class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        A={}
        total=0
        for i in tasks:
            A[i]=A.get(i,0)+1
        l=0
        for i in A:
            if A[i]==max(A.values()):
                l=l+1
        total+=(max(A.values())-1)*(n+1)
        total+=l
        return max(len(tasks),total)

        