class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def d(nums,target):
            result=[]
            if target==0:
                return [[]]
            for i,c in enumerate(nums):
                if c>target:
                    continue
                for rest in d(nums[i:],target-c):
                    result.append([c]+rest)
            return result
        return d(nums,target)
            

        