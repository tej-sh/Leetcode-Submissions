class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)

        dp = [[[-1]*(o+1) for _ in range(n+1)] for _ in range(m+1)]

        def solve(idx1,idx2,idx3):

            if idx1 ==m and idx2 ==n and idx3 == o:
                dp[idx1][idx2][idx3] = True
                return True

            if ( idx1 >= m and idx2 >=n ) or idx3>=o :
                dp[idx1][idx2][idx3] = False
                return False
            take1 = False
            take2 = False
            if dp[idx1][idx2][idx3]!=-1:
                return dp[idx1][idx2][idx3]
            if idx1 < m and s1[idx1] == s3[idx3] :
                take1 = solve(idx1+1,idx2,idx3+1)
            if idx2 < n and s2[idx2] == s3[idx3] :
                take2 = solve(idx1,idx2+1,idx3+1)
            dp[idx1][idx2][idx3] = take1 or take2
            return dp[idx1][idx2][idx3]

        return solve(0,0,0)
