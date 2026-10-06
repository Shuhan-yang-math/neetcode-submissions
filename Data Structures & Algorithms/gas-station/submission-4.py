class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        k=0
        min1=gas[0]-cost[0]
        a=sum(gas)
        b=sum(cost)
        if a<b:
            return -1
        status=gas[0]-cost[0]
        for j in range(1,len(gas)):
            status=status+gas[j]-cost[j]
            if status<=min1:
                k=j
                min1=min(status,min1)
        return k+1 if k<=len(gas)-2 else 0
        

            

        
        