class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] == 1:
                c+=1
                m = max(c,m)
            else:
                c = 0
        return m
