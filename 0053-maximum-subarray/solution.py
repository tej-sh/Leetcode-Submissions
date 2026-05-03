class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxsum = float("-inf")
        for i in range(len(nums)):
            cur = max(cur+nums[i],nums[i])
            maxsum = max(cur,maxsum)
        return maxsum

