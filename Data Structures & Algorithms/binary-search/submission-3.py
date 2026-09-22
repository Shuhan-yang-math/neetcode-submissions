class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        k=(i+j)//2
        while i<=j:
            k=(i+j)//2
            if nums[k]==target:
                return k
            elif nums[k]>target:
                j=k-1
            else:
                i=k+1
        return -1
        