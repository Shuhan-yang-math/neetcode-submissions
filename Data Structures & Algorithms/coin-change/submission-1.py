from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(target):
            if target==0:
                return 0
            if target in coins:
                return 1
            if target<min(coins):
                return float("inf")
            return min([f(target-a)+1 for a in coins])
        if f(amount)>amount:
            return -1
        return f(amount)
        
        