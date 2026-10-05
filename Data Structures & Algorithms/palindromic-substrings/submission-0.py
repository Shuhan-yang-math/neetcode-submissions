class Solution:
    def countSubstrings(self, s: str) -> int:
        nums=0
        n=len(s)
        for i in range(n):
            for left,right in [(i,i),(i,i+1)]:
                while left>=0 and right<=n-1 and s[left]==s[right]:
                    nums+=1
                    left=left-1
                    right=right+1
        return nums

        