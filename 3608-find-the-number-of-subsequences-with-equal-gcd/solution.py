class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        
        import math
        n = len(nums)
        mod = 10**9 + 7
        # dp = [[[-1 for _ in range(201)]for _ in range(201)] for _ in range(201)]
        # # print(dp[0])
        @cache
        def solve(i,j,k):
            if i >=n:
                if j != 0 and k !=0:
                    if j == k:
                        return 1
                    return 0
                return 0
            # if dp[i][j][k] != -1:
            #     return dp[i][j][k]
            skip = solve(i+1,j,k)
            take1 = solve(i+1,math.gcd(j,nums[i]),k)
            take2 = solve(i+1,j,math.gcd(k,nums[i]))
            # dp[i][j][k] = (skip+take1+take2)%mod
            # return dp[i][j][k]
            return (skip+take1+take2)%mod
        return solve(0,0,0)
