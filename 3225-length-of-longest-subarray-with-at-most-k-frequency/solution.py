class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        d = {}
        n = len(nums)
        prev = 0
        mx = 0
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] +=1
                if d[nums[i]] >k:
                    while d[nums[i]] >k:
                        d[nums[prev]]-=1
                        prev+=1
            else:
                d[nums[i]] = 1
            
            mx = max(mx,i-prev+1) 

        return mx
