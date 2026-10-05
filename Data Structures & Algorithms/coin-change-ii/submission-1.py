from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def f(i,target):
            if target==0:
                return 1
            if i>=len(coins) or target<0:
                return 0
            use=f(i,target-coins[i])
            skip=f(i+1,target)
            return use+skip
        return f(0,amount)