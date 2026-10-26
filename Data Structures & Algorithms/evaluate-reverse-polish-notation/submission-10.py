class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        A=[]
        for s in tokens:
            if s not in "+-*/":
                A.append(int(s))
            if s=="+":
                a=A.pop()
                b=A.pop()
                A.append(a+b)
            if s=="-":
                a=A.pop()
                b=A.pop()
                A.append(b-a)
            if s=="*":
                a=A.pop()
                b=A.pop()
                A.append(a*b)
            if s=="/":
                a=A.pop()
                b=A.pop()
                A.append(int(b/a))
        return int(A[0])

        