class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates=deque()
        result=[]
        for i,value in enumerate(nums):
            while candidates and candidates[0]<=i-k:
                candidates.popleft()
            while candidates and nums[candidates[-1]]<=value:
                candidates.pop()
            candidates.append(i)
            if i>=k-1:
                result.append(nums[candidates[0]])
        return result
        