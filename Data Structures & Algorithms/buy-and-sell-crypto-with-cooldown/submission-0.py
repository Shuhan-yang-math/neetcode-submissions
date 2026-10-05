class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        hold=[0]*n
        cash=[0]*n
        hold[0]=-prices[0]
        for i in range(1,n):
            previous=cash[i-2] if i>=2 else 0
            hold[i]=max(hold[i-1],previous-prices[i])
            cash[i]=max(cash[i-1],prices[i]+hold[i-1])
        return cash[-1]        