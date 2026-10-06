from collections import Counter
class CountSquares:

    def __init__(self):
        self.freq=Counter()
        

    def add(self, point: List[int]) -> None:
        x,y=point
        self.freq[(x,y)]+=1
        

    def count(self, point: List[int]) -> int:
        x,y=point
        ans=0
        for (a,b), times in self.freq.items():
            if abs(x-a)!=abs(y-b):
                continue
            if a==x or b==y:
                continue
            ans+=(times*self.freq[(a,y)]*self.freq[(x,b)])
        return ans
        
