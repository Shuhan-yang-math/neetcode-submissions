class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        result=[False]*(n+1)
        result[0]=True
        for i in range(1,n+1):
            for word in wordDict:
                k1=len(word)
                if i>=k1 and result[i-k1]==True and s[i-k1:i]==word:
                    result[i]=True
                    break
        return result[-1]

        