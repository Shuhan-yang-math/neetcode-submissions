class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        O=prerequisites
        A={}
        B={}
        C=[]
        for i in O:
            if i[0] not in A:
                A[i[0]]={i[1]}
            else:
                A[i[0]].add(i[1])
            if i[1] not in B:
                B[i[1]]={i[0]}
            else:
                B[i[1]].add(i[0])
        q=deque([])
        for i in range(numCourses):
            if i not in A:
                q.append(i)
        while q:
            x=q.popleft()
            C.append(x)
            if x not in B:
                continue
            for v in B[x]:
                A[v].discard(x)
                if not A[v]:
                    q.append(v)
        for s in A:
            if A[s]!=set():
                return []
        return C

        

        