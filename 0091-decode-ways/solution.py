class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        valid = [ str(i) for i in range(1,27) ]
        dp = [-1]*(101)
        def solve(idx):
            if idx >= n:
                return 1
            
            if s[idx] not in valid:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            take1 = 0
            take2 = 0

            if s[idx] in valid:
                take1 += solve(idx+1)
            if idx+1 <n and s[idx:idx+2] in valid :
                take2 += solve(idx+2)
            
            dp[idx] = take1 + take2
            return dp[idx]
        return solve(0)
