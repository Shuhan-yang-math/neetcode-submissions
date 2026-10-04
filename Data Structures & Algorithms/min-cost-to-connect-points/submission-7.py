class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        A=set()
        for a in points:
            x1,x2=a
            A.add((x1,x2))
        A.remove((points[0][0],points[0][1]))
        a,b=points[0]
        heap=[(0,a,b)]
        visited=set()
        ans=0
        while heap:
            t,x,y=heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            ans+=t
            if len(visited)==len(points):
                break
            A.discard((x,y))
            for j in A:
                p1,p2=j
                heapq.heappush(heap,(abs(p1-x)+abs(p2-y),p1,p2))
        return ans

        