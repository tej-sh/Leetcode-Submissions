class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [-1]*(n+1)
        
        def solve(i,rem):
            if i == n:
                return True
            if dp[i] != -1:
                return dp[i]
            if rem in wordDict:
                return True
            for j in range(i+1,n+1):
                if s[i:j] in wordDict and solve(j,s[j::]):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return solve(0,s)
