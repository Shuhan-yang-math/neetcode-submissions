class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        A=[grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        if max(A)==0:
            return 0
        s=0
        m=len(grid)
        n=len(grid[0])
        q=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        while q:
            for i in range(len(q)):
                a,b=q.popleft()
                for c,d in[(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
                    if c<0 or c>=m or d<0 or d>=n:
                        continue
                    if grid[c][d]==2 or grid[c][d]==0:
                        continue
                    grid[c][d]+=1
                    q.append((c,d))
            s=s+1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return s-1                
                

        