class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            c = 0
            for j in range(i,n):
                if nums[j] == target:
                    c+=1
                if c > (j-i+1)//2:
                    res +=1
        return res
