class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        from functools import lru_cache
        flag = False
        @lru_cache
        def solve(idx,flag):
            if idx >= len(nums):
                return 0
            
            skip = solve(idx+1,flag)
            val = nums[idx]
            if flag== False:
                val = 0-val
    
            take = val + solve(idx+1, not flag)

            return max(skip,take)
        return solve(0,True)


