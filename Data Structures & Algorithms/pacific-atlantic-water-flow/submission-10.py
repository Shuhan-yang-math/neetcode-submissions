class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        A=[]
        m=len(heights)
        n=len(heights[0])
        def a(i,j):
            s1=0
            s2=0
            q=deque([(i,j)])
            visited={(i,j)}
            while q:
                x,y=q.popleft()
                if x==0 or y==0:
                    s1=1
                if x==m-1 or y==n-1:
                    s2=1
                for c,d in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if c<0 or c>=m or d<0 or d>=n or (c,d) in visited:
                        continue
                    if heights[c][d]<=heights[x][y]:
                        q.append((c,d))
                        visited.add((c,d))    
            if s1*s2==1:
                return True
            return False
        for i1 in range(m):
            for i2 in range(n):
                if a(i1,i2):
                    A.append([i1,i2])
        return A


