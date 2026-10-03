class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        C=set()
        if len(edges)!=n-1:
            return False
        A=[[] for i in range(n)]
        for x,y in edges:
            A[x].append(y)
            A[y].append(x)
        stack=[0]
        C.add(0)
        while stack:
            x=stack.pop()
            for y in A[x]:
                if y not in C:
                    C.add(y)
                    stack.append(y)
        return len(C)==n
        