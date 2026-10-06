class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        A={}
        for i in hand:
            A[i]=A.get(i,0)+1
        for a in hand:
            if A[a]==0:
                continue
            for c in range(a,a+groupSize):
                if c not in A or A[c]==0:
                    return False
                A[c]-=1
        return True
        