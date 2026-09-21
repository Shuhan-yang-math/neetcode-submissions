class MinStack:

    def __init__(self):
        self.A=deque([])
        self.B=deque([])
        

    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.B:
            self.B.append(val)
        else:
            self.B.append(min(val,self.B[-1]))
        

    def pop(self) -> None:
        self.A.pop()
        self.B.pop()
        

    def top(self) -> int:
        return self.A[-1]
        

    def getMin(self) -> int:
        return self.B[-1]
        
