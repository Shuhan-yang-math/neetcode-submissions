class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=[-s for s in stones]
        heapq.heapify(a)
        while len(a)>1:
            x=heapq.heappop(a)
            y=heapq.heappop(a)
            if y>x:
                heapq.heappush(a,-(y-x))
        return -a[0] if a else 0
        