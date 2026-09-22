class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        k=(m+n)//2
        i=0
        j=m*n-1
        def convert(k1):
            return k//n,k%n
        while i<=j:
            k=(i+j)//2
            x1,x2=convert(k)
            if matrix[x1][x2]==target:
                return True
            elif matrix[x1][x2]>target:
                j=k-1
            else:
                i=k+1
        return False

        