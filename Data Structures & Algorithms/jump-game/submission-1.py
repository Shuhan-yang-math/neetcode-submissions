class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=k:
                k=i
        return k==0
        