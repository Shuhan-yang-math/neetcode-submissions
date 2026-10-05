from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def f(s1):
            if not s1:
                return 1
            n=len(s1)
            if s1[0]=='0':
                return 0
            if len(s1)==1:
                return 1
            if s1[-1]=='0':
                if 1<=int(s1[-2]) and int(s1[-2])<=2:
                    return f(s1[:-2])
                return 0
            else:
                if s1[-2]=="0":
                    return f(s1[:-1])
                if int(s1[-1])+int(s1[-2])*10<=26:
                    return f(s1[:-2])+f(s1[:-1])
                else:
                    return f(s1[:-1])
        return f(s)
        