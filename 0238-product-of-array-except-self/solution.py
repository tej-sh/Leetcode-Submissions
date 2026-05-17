class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixproduct = 1
        n = len(nums)
        for i in range(n):
            output.append(prefixproduct)
            prefixproduct *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
