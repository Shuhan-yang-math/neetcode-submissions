class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A={}
        for i in range(len(nums)):
            if target-nums[i] in A:
                return [A[target-nums[i]],i]
            else:
                A[nums[i]]=i
        