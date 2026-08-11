class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        mx = 0
        for i in nums:
            if i-1 in nums:
                continue 
            else:
                cur = i
                count = 1
                
                while cur+1 in nums:
                    count+=1
                    cur+=1
                mx = max(mx,count)
        return mx

            
