class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minval = float("inf")
        ans = False
        for i in range(len(nums)):
            sum1 = 0
            for j in range(i,min((i+r),len(nums))):
                sum1+=nums[j]
                if l<=(j-i+1)<=r and sum1>0:
                    minval = min(minval,sum1)
                    ans=True
        if ans:
            return minval
        else:
            return -1
            
            
