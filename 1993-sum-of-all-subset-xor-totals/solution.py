class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def xor(i,val):
            if i == n:
                return val
            return xor(i+1, val^nums[i]) + xor(i+1,val)
        return xor(0,0)
