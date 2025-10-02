class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        
        c = 0
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            c = i + nums[i]
            mx = max(mx,c)
        return True

