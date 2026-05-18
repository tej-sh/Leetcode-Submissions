class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9+7
        dp = [[[-1]*101 for _ in range(51) ] for _ in range(51) ]
        def solve(idx,sc,mx):

            if idx == n:
                if sc == k:
                    return 1
                return 0
            if dp[idx][sc][mx] != -1:
                return dp[idx][sc][mx]
            result = 0 
            for i in range(1,m+1):
                if i > mx:
                    result += (solve(idx+1,sc+1,i))%mod
                else:
                    result += (solve(idx+1,sc,mx))%mod

            dp[idx][sc][mx] = result%mod
            return dp[idx][sc][mx]
        return solve(0,0,0)
