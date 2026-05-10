class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache
        def solve(rem):
            if rem == 0:
                return 1
            if rem <0:
                return 0
            twostep = 0
            onestep = solve(rem-1)
            twostep = solve(rem-2)
            return onestep+twostep
        
        return solve(n)
