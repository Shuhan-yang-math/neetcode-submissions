from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def f(word3,word4):
            if not word3 or not word4:
                return max(len(word3),len(word4))
            if word3==word4:
                return 0
            else:
                if word3[-1]==word4[-1]:
                    return f(word3[:-1],word4[:-1])
                else:
                    return min(f(word3[:-1],word4[:-1])+1,f(word3,word4[:-1])+1,f(word3[:-1],word4)+1)
        return f(word1,word2)
        