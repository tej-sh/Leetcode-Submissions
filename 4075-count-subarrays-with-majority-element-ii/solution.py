class Solution:
    from collections import defaultdict
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cs = 0
        d=defaultdict(int) 
        d[0] = 1
        res = 0
        valid = 0
        for i in range(n):
            if target == nums[i]:
                valid += d[cs]
                cs+=1
            else:
                cs -=1
                valid -= d[cs]

            d[cs] +=1
            res+=valid
        return res
