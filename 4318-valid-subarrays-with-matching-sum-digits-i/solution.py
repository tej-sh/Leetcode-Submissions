class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        c = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                if str(s)[0] == str(s)[-1] == str(x):
                    c+=1
        return c

