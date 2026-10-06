class Solution:
    def jump(self, nums: List[int]) -> int:
        far=0
        n=len(nums)
        end=0
        jumps=0
        for j in range(n-1):
            far=max(far,nums[j]+j)
            if j==end:
                end=far
                jumps+=1
        return jumps
           
