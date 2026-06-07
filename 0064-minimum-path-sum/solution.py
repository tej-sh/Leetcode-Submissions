class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]

        def solve(i,j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            elif i >= m or j >=n:
                return float("inf")
            if dp[i][j] !=-1:
                return dp[i][j]
            dp[i][j] = min(grid[i][j] + solve(i+1,j),grid[i][j] + solve(i,j+1))
            return dp[i][j]

        return solve(0,0)
