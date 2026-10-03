class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        s=0
        m=len(grid)
        n=len(grid[0])
        max1=0
        def a(i,j):
            nonlocal s
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 
            else:
                s=s+1
                grid[i][j]=0
                a(i+1,j)
                a(i-1,j)
                a(i,j-1)
                a(i,j+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    s=0
                    a(i,j)
                    max1=max(s,max1)
        return max1
        