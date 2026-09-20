class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        result=[]
        for i in range(1,n):
            left[i]=nums[i-1]*left[i-1]
        for j in range(n-2,-1,-1):
            right[j]=nums[j+1]*right[j+1]
        for s in range(n):
            result.append(right[s]*left[s])
        return result
