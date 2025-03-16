class Solution:
    def maxSum(self, nums: List[int]) -> int:
        

        pos = set()
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.add(nums[i])
        
        if pos:
            return sum(pos)
        else:
            return max(nums)
