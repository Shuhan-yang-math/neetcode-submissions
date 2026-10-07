class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        for i in range(0,n+1):
            result^=i
        for j in nums:
            result^=j
        return result
        