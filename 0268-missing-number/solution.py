class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        n = len(nums)
        x = (n*(n+1))//2
        return x-sum1
