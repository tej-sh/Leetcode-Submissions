class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1]*1001 for _ in range(1001)]
        def solve(text1,text2,i,j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1+ solve(text1,text2,i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j] = max(solve(text1,text2,i,j+1),solve(text1,text2,i+1,j))
                return dp[i][j]
        return solve(text1,text2,0,0)
