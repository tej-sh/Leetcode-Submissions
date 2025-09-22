class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mx = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                mx = max(mx,d[i])
            else:
                d[i] = 1
                mx = max(mx,d[i])
        ans = 0
        for i in d:
            if d[i] == mx:
                ans+=mx
        return ans
