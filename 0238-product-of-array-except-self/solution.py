class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pa = [0]*len(nums)
        sa = []
        s = 1
        for i in nums:
            sa.append(s)
            s *= i
        p = 1
        for j in range(len(nums)-1,-1,-1):
            pa[j] = p
            p *= nums[j]
        return [sa[i]*pa[i] for i in range(len(nums)) ]
