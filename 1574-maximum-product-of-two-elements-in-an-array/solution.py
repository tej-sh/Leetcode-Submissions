class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1 = max(nums)
        nums.remove(mx1)
        mx2 = max(nums)
        return (mx1-1)*(mx2 -1)
