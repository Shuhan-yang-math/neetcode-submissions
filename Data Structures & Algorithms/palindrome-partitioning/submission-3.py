class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def d(t):
            if t=='':
                return [[]]
            result=[]
            for i in range(1,len(t)+1):
                A=t[:i]
                if A!=A[::-1]:
                    continue
                for rest in d(t[i:]):
                    result.append([A]+rest)
            return result
        return d(s)
        