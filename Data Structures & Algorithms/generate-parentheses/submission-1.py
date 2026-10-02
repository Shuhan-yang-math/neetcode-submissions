class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def d(s,left,right):
            if left==n and right==n:
                result.append(s)
                return
            if left<n:
                d(s+"(",left+1,right)
            if right<left:
                d(s+")",left,right+1)
        d("",0,0)
        return result