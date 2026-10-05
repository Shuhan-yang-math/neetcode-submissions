class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=min1=ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            p=x*max1
            q=x*min1
            max1=max(x,p,q)
            min1=min(x,p,q)
            ans=max(ans,max1)
        return ans
        