class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s=0
        n=len(edges)
        parents=[i for i in range(n)]
        size=[1]*n
        def find(a):
            while a!=parents[a]:
                parents[a]=parents[parents[a]]
                a=parents[a]
            return a
        for j in range(n):
            a,b=edges[j]
            a=a-1
            b=b-1
            a=find(a)
            b=find(b)
            if a==b:
                s=j
            else:
                if size[a]<size[b]:
                    a,b=b,a
                parents[b]=a
                size[a]+=size[b]
        return edges[s]

            

        