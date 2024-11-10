class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def up(start):
            for i in range(start ,start+k-1):
                if nums[i]>= nums[i+1]:
                    return False
            return True
        for i in range(n-2*k+1):
            if up(i) and up(i+k):
                return True
        return False
                
