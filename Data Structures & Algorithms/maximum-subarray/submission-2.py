class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max2=nums[0]
        max1=nums[0]
        for i in range(1,len(nums)):
            if max1>0:
                max1=max1+nums[i]
                max2=max(max1,max2)
            else:
                max1=nums[i]
                max2=max(max1,max2)
        return max2
        