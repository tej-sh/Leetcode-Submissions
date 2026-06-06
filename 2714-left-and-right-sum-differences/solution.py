class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = []
        suf = [0]*n
        s = 0
        for i in nums:
            s += i
            p.append(s)
    
        s = 0
        for i in range(n-1,-1,-1):
            s+=nums[i]
            suf[i] = s
        
        for i in range(n):
            suf[i] = abs(suf[i] - p[i])
        
        return suf
