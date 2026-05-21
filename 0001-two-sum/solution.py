class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d: 
                return [d[target-nums[i]] , i]

            else:
                d[nums[i]] = i
        
        
        
