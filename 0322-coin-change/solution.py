class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [[-1]*(amount+1) for _ in range(n+1) ]
        def solve(idx,rem):
            if rem == 0:
                return 0
            if idx >=n:
                return float("inf")
            if dp[idx][rem] != -1:
                return dp[idx][rem]

            take = float("inf")
            if rem >= coins[idx]:
                take = 1 + solve(idx,rem-coins[idx])
            skip = solve(idx+1,rem)
            dp[idx][rem] = min(skip,take)
            return dp[idx][rem]
        ans = solve(0,amount)
        return -1 if ans == float("inf") else ans
        
        
