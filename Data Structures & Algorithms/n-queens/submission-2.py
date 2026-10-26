class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        queens=[]
        columns=set()
        diag_diff=set()
        diag_sum=set()
        def backtrack(row):
            if row==n:
                result.append([
                    "."*col+"Q"+"."*(n-col-1)
                    for col in queens
                ])
                return 
            for col in range(n):
                diff=row-col
                total=row+col
                if (col in columns or
                        diff in diag_diff or 
                        total in diag_sum):
                    continue
                queens.append(col)
                columns.add(col)
                diag_diff.add(diff)
                diag_sum.add(total)
                backtrack(row+1)
                queens.pop()
                columns.remove(col)
                diag_diff.remove(diff)
                diag_sum.remove(total)
        backtrack(0)
        return result
        