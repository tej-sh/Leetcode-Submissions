class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n+1)]
        def solve(idx,rem):
            if rem == 0:
                return 1
            if idx >=n:
                return 0
            
            if rem < coins[idx]:
                return solve(idx+1,rem)
            if dp[idx][rem] != -1:
                return dp[idx][rem]
            take = 0
            if rem >= coins[idx]:
                take = solve(idx,rem-coins[idx])
            skip = solve(idx+1,rem)
            dp[idx][rem] = skip + take
            return dp[idx][rem]
        return solve(0,amount)
        
