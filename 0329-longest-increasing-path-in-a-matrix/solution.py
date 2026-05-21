class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1]*(n+1) for _ in range(m+1)]

        def solve(i,j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            up,down,left,right = 1,1,1,1

            if i+1<m and matrix[i][j] < matrix[i+1][j] :
                down = 1+solve(i+1,j)

            if j+1<n and matrix[i][j] < matrix[i][j+1] :
                right = 1+solve(i,j+1)

            if j-1 > -1 and matrix[i][j] < matrix[i][j-1] :
                left = 1+solve(i,j-1)

            if i-1 > -1 and matrix[i][j] < matrix[i-1][j] :
                up = 1+solve(i-1,j)
            dp[i][j] = max(up,down,left,right)
            return dp[i][j]

        res = float("-inf")

        for i in range(m):
                for j in range(n):
                    res = max(res,solve(i,j))
        
        return res
                    
