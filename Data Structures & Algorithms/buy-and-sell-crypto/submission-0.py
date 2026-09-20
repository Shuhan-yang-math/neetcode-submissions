class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1=0
        minq=float("inf")
        for i in range(len(prices)):
            minq=min(prices[i],minq)
            max1=max(max1,prices[i]-minq)
        return max1
        