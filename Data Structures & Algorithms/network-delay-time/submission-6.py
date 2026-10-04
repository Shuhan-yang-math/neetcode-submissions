class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u1,v1,t1 in times:
            graph[u1].append((v1,t1))
        heap=[(0,k)]
        visited=set()
        ans=0
        while heap:
            a,b=heapq.heappop(heap)
            if b in visited:
                continue
            visited.add(b)
            ans=a
            for i1,j1 in graph[b]:
                if i1 not in visited:
                    heapq.heappush(heap,(a+j1,i1))
        return ans if len(visited)==n else -1
        