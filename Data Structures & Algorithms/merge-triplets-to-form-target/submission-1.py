class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found=[False,False,False]
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]:
                found[0]=True
            if b==target[1]:
                found[1]=True
            if c==target[2]:
                found[2]=True
        return all(found)
        