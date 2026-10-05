from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k=sum(nums)
        if k%2!=0:
            return False
        s=k//2
        @cache
        def f(i,target):
            if target==0:
                return True
            if target <0 or i==len(nums):
                return False
            return (
                f(i+1,target-nums[i]) or f(i+1,target)
            )
        return f(0,s)