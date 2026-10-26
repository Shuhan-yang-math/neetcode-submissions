class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ""
        need=Counter(t)
        window={}
        formed=0
        required=len(need)
        left=0
        best_start=0
        best_len=len(s)+1
        for right,char in enumerate(s):
            if char in need:
                window[char]=window.get(char,0)+1
                if window[char]==need[char]:
                    formed+=1
            while formed==required:
                length=right-left+1
                if length<best_len:
                    best_start=left
                    best_len=length
                outgoing=s[left]
                if outgoing in need:
                    window[outgoing]-=1
                    if window[outgoing]<need[outgoing]:
                        formed-=1
                left+=1
        if best_len==len(s)+1:
            return ""
        return s[best_start:best_start+best_len]

        