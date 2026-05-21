class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[-1]*n for _ in range(m)]
        def solve(i,j):
            if j==n:
                return 1

            if i >=m or j>=n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            take = 0
            skip = 0
            if s[i] == t[j]:
                take += solve(i+1,j+1)
            skip += solve(i+1,j)
            dp[i][j] = take+skip
            return dp[i][j]

        return solve(0,0)
