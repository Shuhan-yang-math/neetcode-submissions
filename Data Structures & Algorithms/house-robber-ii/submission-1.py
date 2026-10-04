class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        choice1=[0]*(len(nums)-1)
        choice2=[0]*(len(nums)-1)
        choice1[0]=nums[0]
        choice1[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            choice1[i]=max(choice1[i-1],nums[i]+choice1[i-2])
        choice2[0]=nums[1]
        choice2[1]=max(nums[1],nums[2])
        for i in range(2,len(nums)-1):
            choice2[i]=max(choice2[i-1],nums[i+1]+choice2[i-2])
        return max(choice1[-1],choice2[-1])
        