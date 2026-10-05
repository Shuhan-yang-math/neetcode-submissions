from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def f(i,target):
            if i==0:
                if nums[i]==target and nums[i]==-target:
                    return 2
                elif nums[i]==target:
                    return 1
                elif nums[i]==-target:
                    return 1
                else:
                    return 0
            return f(i-1,target-nums[i])+f(i-1,target+nums[i])
        return f(len(nums)-1,target)