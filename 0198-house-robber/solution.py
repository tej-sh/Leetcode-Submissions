class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        n = len(nums)
        @lru_cache
        

        def solve(idx):
            if idx>= n:
                return 0
            take = nums[idx] + solve(idx+2)
            skip = solve(idx+1)

            return max(skip,take)
        
        return solve(0)
