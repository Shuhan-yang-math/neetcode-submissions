class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def d(a):
            a.sort()
            result=[[]]
            for i,x in enumerate(a):
                if i>0 and a[i]==a[i-1]:
                    continue
                for j in d(a[i+1:]):
                    result.append([x]+j)
            return result
        return d(nums)
        