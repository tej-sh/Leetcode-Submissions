class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache
        def solve(idx):
            if idx == n:
                return 1
            if idx>n:
                return 0
            take = solve(idx+1)
            take2 = solve(idx+2)
            return take+take2
        return solve(0)
