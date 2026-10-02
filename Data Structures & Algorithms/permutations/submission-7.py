class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def d(a):
            if len(a)==0:
                return [[]]
            result=[]
            for i,c in enumerate(a):
                for j in d(a[:i]+a[i+1:]):
                    result.append([c]+j)
            return result
        return d(nums)

        