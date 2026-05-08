class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        n = len(nums)
        @lru_cache(None)
        
        def solve(i):
            if i>=n:
                return 0
            
            steal =nums[i] + solve(i+2)
            skip = solve(i+1)
            return max(steal,skip)
        
        if n == 0:
            return 0
        
        if n==1:
            return nums[0]

        return solve(0)

