class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        from functools import lru_cache
        n = len(cost)

        @lru_cache
        def solve(idx):
            if idx >= n:
                return 0
            
            onestep = cost[idx]+solve(idx+1)
            twostep = cost[idx] + solve(idx+2)
            return min(onestep,twostep)

        if n==0:
            return 0
        if n==1 :
            return cost[0]
        
        return min(solve(0),solve(1))
