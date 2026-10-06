class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in digits:
            a=a*10+i
        a=a+1
        b=str(a)
        A=[]
        for i in b:
            A.append(int(i))
        return A
        