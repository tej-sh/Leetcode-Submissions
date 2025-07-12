class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = sorted(nums)
        l =  l[len(nums)-k:len(nums)]
        ans = []
        for i in nums:
            if i in l:
                l.remove(i)
                ans.append(i)
        return ans
