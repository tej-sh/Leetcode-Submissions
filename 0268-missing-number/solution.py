class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sn = (n+1)*n//2
        return sn-sum(nums)
