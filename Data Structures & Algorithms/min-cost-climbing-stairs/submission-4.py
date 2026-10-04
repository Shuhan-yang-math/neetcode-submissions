from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def f(n):
            if n==0:
                return 0
            if n==1:
                return 0
            return min(f(n-1)+cost[n-1],f(n-2)+cost[n-2])
        return min(f(len(cost)-1)+cost[-1],f(len(cost)-2)+cost[-2])
        