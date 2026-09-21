class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=1
        for i in range(len(s)):
            if i>0 and s[i]==s[i-1]:
                continue
            q=k
            for j in range(i+1,len(s)):
                if s[j]!=s[i]:
                    q=q-1
                    if q==-1:
                        l=max(l,j-i)
            if q>=0:
                l=min(len(s),max(l,len(s)-i+q))
        return l

        