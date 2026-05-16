class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = float("inf")
        n = len(nums)
        s = 0
        l = 0
        prev = 0


        for i in range(n):
            s += nums[i]
            l += 1
            while target <= s :
                mn = min(mn,l)
                s-= nums[prev]
                prev = prev+1
                if l >0:
                    l -= 1
        return mn if mn!= float("inf") else 0
