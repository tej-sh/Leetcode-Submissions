class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            s = 0
            if i-k >=0:
                if nums[i-k] < nums[i]:
                    s+=1
            else:
                s+=1
            if i+k <=len(nums)-1:
                if nums[i+k]<nums[i]:
                    s+=1
            else:
                s+=1
            if s==2:
                ans+=nums[i]
        return ans
