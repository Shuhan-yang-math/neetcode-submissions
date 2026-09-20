class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            A=set()
            for j in range(len(board)):
                if board[i][j]!='.':
                    if board[i][j] in A:
                        return False
                    else:
                        A.add(board[i][j])
        for i in range(len(board)):
            B=set()
            for j in range(len(board)):
                if board[j][i]!='.':
                    if board[j][i] in B:
                        return False
                    else:
                        B.add(board[j][i])
        for s in range(3):
            for j in range(3):
                C=set()
                for a in range(3):
                    for b in range(3):
                        if board[3*s+a][3*j+b]!='.':
                            if board[3*s+a][3*j+b] in C:
                                return False
                            else:
                                C.add(board[3*s+a][3*j+b])
        return True



        