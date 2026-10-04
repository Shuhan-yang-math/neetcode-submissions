from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n<=0:
                return 0
            return f(n-1)+f(n-2)
        return f(n)
        