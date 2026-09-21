class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        k=n
        A=[]
        for i in range(n):
            A.append([position[i],speed[i]])
        B=sorted(A,key=lambda x:x[0])
        for j in range(n-1,0,-1):
            if (target-B[j-1][0])/B[j-1][1]<=(target-B[j][0])/B[j][1]:
                k=k-1
                B[j-1]=B[j]
        return k