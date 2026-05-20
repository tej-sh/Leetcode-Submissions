class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[[-1]*2 for _ in range(2)] for _ in range(n)]
        print(dp)
        def solve(idx,cooldown,holding):
            if idx>=n:
                return 0
            if dp[idx][cooldown][holding]!= -1:
                return dp[idx][cooldown][holding]
            if holding:
                sell = prices[idx] + solve(idx+1,1,0)
                later = solve(idx+1,cooldown,holding)
                dp[idx][cooldown][holding] =  max(sell,later)
                return dp[idx][cooldown][holding]
            buy = 0
            skip = 0
            if not holding:
                if cooldown:
                    skip = solve(idx+1,0,holding)
                else:
                    buy =  - prices[idx] + solve(idx+1,cooldown,1)
                    skip = solve(idx+1,cooldown,holding) 
            dp[idx][cooldown][holding] = max(buy,skip) 
            return dp[idx][cooldown][holding]
        # def solve(idx,cd,bp):
            # if idx>=n:
            #     return 0
            # if bp!=-1:
            #     sellnow = (prices[idx] - bp) + solve(idx+1,1,-1)
            #     sellLater = solve(idx+1,cd,bp)
            #     return max(sellnow,sellater)

            # buy = -1
            # if cd == 0:
            #     buy= solve(idx+1,cd,prices[idx])
            # else:
            #     skip = solve(idx+1,cd-1,bp)
            # skip = solve(idx+1,cd,bp)
            # return max(buy,skip)
        return solve(0,0,0)
