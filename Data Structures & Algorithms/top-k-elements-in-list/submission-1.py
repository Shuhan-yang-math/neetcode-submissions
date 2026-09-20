class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A={}
        B=[]
        for i in nums:
            A[i]=A.get(i,1)+1
        for a,d in A.items():
            B.append([a,d])
        B.sort(key=lambda x:x[1])
        r=[]
        for c in range(k):
            r.append(B[len(B)-1-c][0])
        return r



        