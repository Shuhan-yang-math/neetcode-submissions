class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A={}
        for i in nums:
            if i not in A:
                A[i]=A.get(i,0)+1
            else:
                return True
        return False
        