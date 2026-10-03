class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        def a(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 
            if board[i][j]!="O":
                return
            board[i][j]="#"
            a(i-1,j)
            a(i+1,j)
            a(i,j-1)
            a(i,j+1)
        for i in range(m):
            a(i,0)
            a(i,n-1)
        for j in range(n):
            a(0,j)
            a(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="#":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"

        