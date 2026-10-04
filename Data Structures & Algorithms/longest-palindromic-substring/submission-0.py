class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        max1=0
        for i in range(len(s)):
            for p,q in [(i,i),(i,i+1)]:
                while p>=0 and q<=len(s)-1 and s[p]==s[q]:
                    length=q-p+1
                    if length>=max1:
                        start=p
                    max1=max(max1,length)
                    p=p-1
                    q=q+1
        return s[start:start+max1]
        