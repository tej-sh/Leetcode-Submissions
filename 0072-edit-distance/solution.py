class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if j>=n and i>=m:
                return 0
            if j>=n:
                return m-i
            if dp[i][j] !=-1:
                return dp[i][j]
            if i>=m:
                insert = 1+ solve(i,j+1)
                return insert
            else:
                take = float("inf")
                if word1[i] == word2[j] :
                    take = solve(i+1,j+1)
                insert = 1+solve(i,j+1)
                replace = 1+solve(i+1,j+1)
                delete = 1+solve(i+1,j)
                dp[i][j] = min(take,replace,delete,insert)
                return dp[i][j]
        return solve(0,0)
