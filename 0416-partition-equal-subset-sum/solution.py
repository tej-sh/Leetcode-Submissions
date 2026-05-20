class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:
            return False
        total = sum(nums)
        dp = [[-1]*(total+1) for _ in range(n+1)]
        def solve(i,cursum):
            if i>=n:
                return cursum == total/2
            if dp[i][cursum] != -1:
                return dp[i][cursum]

            take = solve(i+1,cursum-nums[i])
            nottake = solve(i+1,cursum)
            dp[i][cursum]=take or nottake
            return dp[i][cursum]

        return solve(0,total)

