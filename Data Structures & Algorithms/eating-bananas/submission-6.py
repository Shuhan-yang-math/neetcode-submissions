class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=sum(piles)
        k=(i+j)//2
        def cal(a,k):
            q=0
            for i in range(len(a)):
                if a[i]%k==0:
                    q=q+(piles[i]//k)
                else:
                    q+=(piles[i]//k)+1
            return q
        while i<=j:
            k=(i+j)//2
            if k>1 and cal(piles,k)<=h and cal(piles,k-1)>h:
                return k
            elif k>1 and cal(piles,k-1)<=h:
                j=k-1
            elif cal(piles,k)>h:
                i=k+1
            else:
                return 1
        return 1
        

        