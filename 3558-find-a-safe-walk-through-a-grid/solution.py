class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        dp = [[[-1 for _ in range(health+1)] for _ in range(m+1)] for _ in range(n)]

        def solve(i,j,health):
            if i>=n or j>=m or i<0 or j<0:
                return False
            
            if dp[i][j][health] != -1:
                return dp[i][j][health]
            
            nhealth = health
            if grid[i][j] == 1:
                nhealth =health-1 
                if nhealth <1:
                    return False
            if i == n-1 and j == m-1:
                return True


            dp[i][j][health]= False
            down = solve(i+1,j,nhealth)
            right = solve(i,j+1,nhealth)
            up =solve(i-1,j,nhealth)
            left =solve(i,j-1,nhealth)

            dp[i][j][health] =  down or right or up or left
            return dp[i][j][health]

        return solve(0,0,health)
