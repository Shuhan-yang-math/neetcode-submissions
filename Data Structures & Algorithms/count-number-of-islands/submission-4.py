class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def a(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return
            else:
                grid[i][j]="0"
                a(i+1,j)
                a(i-1,j)
                a(i,j-1)
                a(i,j+1)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    a(i,j)
        return count
        