class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        k=(i+j)//2
        result=float("inf")
        while i<=j:
            k=(i+j)//2
            if nums[i]<=nums[k]:
                result=min(nums[i],result)
                i=k+1
            else:
                result=min(result,nums[k])
                j=k-1
        return result
        