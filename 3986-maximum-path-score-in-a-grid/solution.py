class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # from functools import lru_cache
        # @lru_cache()
        def solve(i,j,c):
            if i == m-1 and j==n-1:
                if c+costChart[grid[i][j]] <= k:
                    return grid[i][j]
                return float("-inf")
            
            if i >= m or j>=n:
                return float("-inf")
            if c > k:
                return float("-inf")
            if dp[i][j][c] != -1:
                return dp[i][j][c]
            right = grid[i][j]+solve(i,j+1,c+costChart[grid[i][j]])
            down = grid[i][j]+solve(i+1,j,c+costChart[grid[i][j]])

            dp[i][j][c] = max(right,down)
            return dp[i][j][c]

        m = len(grid)
        n = len(grid[0])
        
        costChart = {
            0 : 0,
            1 : 1,
            2 : 1
        }

        dp = [[[-1]*(k+1) for _ in range(n) ] for _ in range(m)]

        res = solve(0,0,0)
        return res if res != float("-inf") else -1
