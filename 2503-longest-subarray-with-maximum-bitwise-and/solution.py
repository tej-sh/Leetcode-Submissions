class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x = max(nums)
        c = 0 
        mx = 0
        for i in range(len(nums)):
            if nums[i] == x:
                c+=1
                mx = max(c,mx)
            else:
                c = 0
        return mx
