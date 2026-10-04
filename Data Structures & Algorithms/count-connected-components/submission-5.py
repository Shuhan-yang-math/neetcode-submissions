class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents=[i for i in range(n)]
        size=[1]*n
        count=n
        def find(x):
            while x!=parents[x]:
                parents[x]=parents[parents[x]]
                x=parents[x]
            return x
        for a,b in edges:
            x1=find(a)
            x2=find(b)

            if x1==x2:
                continue
            else:
                if size[x1]<size[x2]:
                    x1,x2=x2,x1
                parents[x2]=x1
                size[x1]+=size[x2]
                count-=1
        return count
        