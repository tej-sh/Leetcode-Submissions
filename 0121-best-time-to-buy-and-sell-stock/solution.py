class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        mn = float("inf")
        mx = float("-inf")
        for i in range(len(prices)):
            if mn > prices[i]:
                mn = prices[i]
                mx = prices[i]
            else:
                mx = max(mx,prices[i])
                maxprofit = max( maxprofit,mx - mn)
        return maxprofit
