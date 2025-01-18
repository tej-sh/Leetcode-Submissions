class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = -999999
        for i in range(len(nums)-1):
            diff = max(diff,abs(nums[i]-nums[i+1]))
        diff= max(diff,abs(nums[0]-nums[len(nums)-1]))
        return diff
        
