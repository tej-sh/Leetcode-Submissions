class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid,nums):
            i = 0
            robbed = 0
            while i < len(nums):
                if nums[i] <=mid:
                    i+=1
                    robbed+=1
                    if robbed == k:
                        return True
                i+=1
            return False

        low = min(nums)
        high = max(nums)
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            if check(mid,nums):
                ans = min(ans,mid)
                high = mid-1
            else:
                low = mid+1
        return ans
