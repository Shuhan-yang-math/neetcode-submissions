class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A={}
        for i in nums:
            if i not in A:
                A[i]=0
            else:
                return True
        return False
        