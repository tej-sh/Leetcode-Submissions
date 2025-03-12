import bisect
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        idx = bisect.bisect_right(nums,-1)
        idx2 = bisect.bisect_left(nums,1)
        n = len(nums)
        # print(idx)
        # print(idx2)
        # print(n)
        # print(n-idx2)
        return (max(idx,len(nums)-idx2))

