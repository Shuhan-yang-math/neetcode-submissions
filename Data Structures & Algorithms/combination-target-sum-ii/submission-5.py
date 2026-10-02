class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def d(nums,target):
            nums.sort()
            if target==0:
                return [[]]
            result=[]
            for i,x in enumerate(nums):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                if x>target:
                    continue
                for rest in d(nums[i+1:],target-x):
                    result.append([x]+rest)
            return result
        return d(candidates,target)
        