class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*101 for _ in range(101)]
        def solve(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j == n-1:
                if obstacleGrid[i][j] == 1:
                    return 0
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            
            dp[i][j] = solve(i+1,j) + solve(i,j+1)
            return dp[i][j] 
        return solve(0,0)
