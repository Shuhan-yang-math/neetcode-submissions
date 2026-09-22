class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        k=(i+j)//2
        while i<=j:
            k=(i+j)//2
            if nums[k]==target:
                return k
            if nums[i]<=nums[k]:
                if nums[i]<=target<nums[k]:
                    j=k-1
                else:
                    i=k+1
            elif nums[i]>nums[k]:
                if nums[j]>=target>nums[k]:
                    i=k+1
                else:
                    j=k-1
        return -1

        
        