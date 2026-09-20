class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max1=0
        while i<j:
            max1=max(max1,min(heights[i],heights[j])*(j-i))
            if heights[i]<=heights[j]:
                i=i+1
            else:
                j=j-1
        return max1

        