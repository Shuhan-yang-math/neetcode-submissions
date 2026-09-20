class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        l=0
        right=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            right=i
            l=max(right-left+1,l)
        return l
        
        