class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            c = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    c+=1
            ans.append(c)
        return ans
