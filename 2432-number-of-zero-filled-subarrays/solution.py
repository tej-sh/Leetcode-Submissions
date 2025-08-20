class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        c = 0
        p1 = 0
        while p1 < len(nums):
            if nums[p1] == 0:
                c+=1
            else:
                res += (c*(c+1))//2
                c = 0
            p1+=1
        
        res += (c*(c+1))//2
        return res
