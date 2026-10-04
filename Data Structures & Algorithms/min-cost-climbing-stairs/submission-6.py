class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c=[0]*len(cost)
        if len(cost)<=2:
            return min(cost)
        for i in range(2,len(cost)):
            c[i]=min(c[i-2]+cost[i-2],c[i-1]+cost[i-1])
        return min(c[-2]+cost[-2],c[-1]+cost[-1])


        