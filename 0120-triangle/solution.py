class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*i for i in range(1,n+1)]
        

        # for i in range(n-1,-1,-1):
        #     for j in range(len(traingle[i])+1):
        #         dp[j] = min(triangle[i][j]+dp[j-1] )

        # memo = {}
        @cache
        def solve(i,j):
            if i >= n:
                return 0
            if dp[i][j] != -1:
                
                return dp[i][j]

            take1 = triangle[i][j]+solve(i+1,j)
            take2 = triangle[i][j] + solve(i+1,j+1)
            
            dp[i][j] =  min(take1,take2) 
            return dp[i][j]
        
        return solve(0,0)
