class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = 0
        for i in range(1,n):
            if prices[i-1] < prices[i]:
                p+= prices[i] - prices[i-1]

        return p        
        
        
        
        
        
        
        # minarr = [0]*n
        # prof = [0]*n
        # s = prices[0]
        # minarr[0] = s
        # for i in range(1,n):
        #     if s > prices[i]:
        #         s = prices[i]
        #     minarr[i] = s
        # prof = [0]*n
        # for i in range(n):
        #     prof[i] = prices[i] - minarr[i]
        # print(minarr)
        # print(prof)
