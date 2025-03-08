class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        t = nums[0]
        for i in range(1,n):
            t = max(nums[i],t+nums[i])
            res = max(t,res)
        return res
