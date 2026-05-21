class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        n = len(nums)
        memo = {}
        def solve(idx,sm):
            if sm == target and idx == n:
                memo[(idx,sm)] = 1
                return 1
            if idx >=n:
                memo[(idx,sm)] = 0
                return 0
            if (idx,sm) in memo:
                return memo[(idx,sm)]
            plus = solve(idx+1,sm+nums[idx]) 
            minus = solve(idx+1,sm-nums[idx])
            memo[(idx,sm)] = plus+minus
            return memo[(idx,sm)]

        return solve(0,0)
