class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A=set(nums)
        b=0
        for a in A:
            if a-1 in A:
                continue
            else:
                length=1
                while a+length in A:
                    length=length+1
                b=max(b,length)
        return b