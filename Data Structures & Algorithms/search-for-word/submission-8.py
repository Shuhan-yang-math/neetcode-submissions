class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        k=len(word)
        A=set()
        def search(a1,a2,k1):
            if a1<0 or a1>m-1 or a2<0 or a2>n-1 or (a1,a2) in A:
                return False
            if board[a1][a2]!=word[k1]:
                return False
            if board[a1][a2]==word[k-1] and k1==k-1:
                return True
            if board[a1][a2]==word[k1]:
                A.add((a1,a2))
                x1=search(a1-1,a2,k1+1) or search(a1,a2-1,k1+1) or search(a1,a2+1,k1+1) or search(a1+1,a2,k1+1)
                A.remove((a1,a2))
            return x1
        for i in range(m):
            for j in range(n):
                if search(i,j,0):
                    return True
        return False
        