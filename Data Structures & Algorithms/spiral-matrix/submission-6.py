class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        A=[]
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        while top<bottom and left<right:
            for i in range(left,right):
                A.append(matrix[top][i])
            top=top+1
            for i in range(top,bottom):
                A.append(matrix[i][right-1])
            right=right-1
            if top<bottom:
                for i in range(right-1,left-1,-1):
                    A.append(matrix[bottom-1][i])
                bottom=bottom-1
            if left<right:
                for i in range(bottom-1,top-1,-1):
                    A.append(matrix[i][left])
                left=left+1
        return A
        