from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def valid(s11,s21,s31):
            if not s11:
                return s21==s31
            if not s21:
                return s11==s31
            if s31[-1]==s11[-1]:
                return valid(s11[:-1],s21,s31[:-1])
            elif s31[-1]==s21[-1]:
                return valid(s11,s21[:-1],s31[:-1])
            else:
                return False
        return valid(s1,s2,s3)
        