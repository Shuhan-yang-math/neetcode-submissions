from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def f(i,holding):
            if i>=n:
                return 0
            if holding:
                sell=prices[i]+f(i+2,False)
                return max(f(i+1,holding),sell)
            else:
                buy=-prices[i]+f(i+1,True)
                return max(buy,f(i+1,False))
        return f(0,False)

        