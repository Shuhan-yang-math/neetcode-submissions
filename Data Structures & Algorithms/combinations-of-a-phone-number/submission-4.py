class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        A={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if not digits:
            return []
        def d(s):
            if len(s)==0:
                return [""]
            result=[]
            for i in A[s[0]]:
                for p in d(s[1:]):
                    result.append(i+p)
            return result
        return d(digits)

        