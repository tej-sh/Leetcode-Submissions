class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*(n)
        prev = [-1]*(n)
        maxl = 1
        max_idx = 0

        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        prev[i] = j
                    if maxl < dp[i]:
                        maxl = dp[i]
                        max_idx = i
        res = []
        if n == 1:
            return nums
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        return res

                
        
