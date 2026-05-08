class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = [0]*(n+1)
        res[1] = nums[0]
        for i in range(2,n):
            steal = nums[i-1]+res[i-2]
            skip =  res[i-1]
            
            res[i] = max(steal,skip)
        res1 = res[n-1]
        res =[0]*(n+1)
        for i in range(2,n+1):
            steal = nums[i-1]+res[i-2]
            skip = res[i-1]
            res[i] = max(steal,skip)

        res2 = res[n]

        return max(res1,res2)
