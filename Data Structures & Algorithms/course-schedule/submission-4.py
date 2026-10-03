class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        B=prerequisites
        A={}
        C={}
        for i in B:
            if i[0] not in A:
                A[i[0]]={i[1]}
            else:
                A[i[0]].add(i[1])
            if i[1] not in C:
                C[i[1]]={i[0]}
            else:
                C[i[1]].add(i[0])
        q=deque([])
        for b in range(numCourses):
            if b not in A:
                q.append(b)
        while q:
            x=q.popleft()
            if x not in C:
                continue
            for c in C[x]:
                if x in A[c]:
                    A[c].remove(x)
                    if A[c]==set():
                        q.append(c)
        for j in A:
            if A[j]!=set():
                return False
        return True
