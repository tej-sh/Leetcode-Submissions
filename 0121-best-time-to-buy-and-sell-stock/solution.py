class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mn = float('inf')
        mx = float('-inf')
        profit = 0
        for i in range(n):
            if prices[i] < mn :
                mn = prices[i]
                mx = prices[i]
            else:
                mx = max(mx,prices[i])
                profit = max(profit,mx - mn ) 
        return profit

            

