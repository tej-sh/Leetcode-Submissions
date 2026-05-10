class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)]

        
        def solve(idx,prev):
            if idx>=n:
                return 0
            if prev!= -1 and dp[idx][prev] !=-1:
                return dp[idx][prev]
            take = 0
            if prev == -1 or nums[idx] > nums[prev] :
                take = 1+solve(idx+1,idx)
            
            skip = solve(idx+1,prev)

            if prev !=-1:
                dp[idx][prev] = max(skip,take)

            return max(skip,take)
        if n==0:
            return 0
        if n==1:
            return 1

        return solve(0,-1)
        


