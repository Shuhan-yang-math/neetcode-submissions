class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for j in nums:
            a=[]
            for c in result:
                a.append([j]+c)
            result.extend(a)
        return result
        