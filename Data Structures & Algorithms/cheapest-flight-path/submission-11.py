class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        A=defaultdict(list)
        for i in flights:
            a1,a2,a3=i
            A[a1].append((a2,a3))
        heap=[(0,0,src)]
        visited=set()
        while heap:
            k1,k2,k3=heapq.heappop(heap)
            if (k2,k3) in visited:
                continue
            visited.add((k2,k3))
            if k3==dst and k2<=k+1:
                return k1
            if k2==k+1:
                continue
            for c in A[k3]:
                x1,y1=c
                heapq.heappush(heap,(k1+y1,k2+1,x1))
        return -1
        
            

        