class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        a=0 in matrix[0]
        b=False
        for i in range(m):
            if matrix[i][0]==0:
                b=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if a:
            for i in range(n):
                matrix[0][i]=0
        if b:
            for j in range(m):
                matrix[j][0]=0
                
        