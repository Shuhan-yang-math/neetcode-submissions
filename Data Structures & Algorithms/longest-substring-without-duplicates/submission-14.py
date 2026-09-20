class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        l=0
        A=set()
        n=len(s)
        for i in range(n):
            while s[i] in A:
                A.remove(s[left])
                left=left+1
            A.add(s[i])
            l=max(i-left+1,l)
        return l
            
        