class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        r=[]
        for a in strs:
            kkk=str(sorted(a))
            if kkk not in s:
                s[kkk]=[a]
            else:
                s[kkk].append(a)
        for b in s.values():
            r.append(b)
        return r

            
        
        

        