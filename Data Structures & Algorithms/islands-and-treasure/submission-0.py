class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            i,j=q.popleft()
            for c,d in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if c<0 or c>=m or d<0 or d>=n:
                    continue
                if grid[c][d]!=2147483647:
                    continue
                grid[c][d]=grid[i][j]+1
                q.append((c,d))



        