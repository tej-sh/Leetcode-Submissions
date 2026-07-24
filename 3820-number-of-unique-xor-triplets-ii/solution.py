class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()
        nums = list(set(nums))
        n =len(nums)
        for i in range(n):
            for j in range(i,n):
                if (nums[i],nums[j]) not in s:
                    s.add(nums[i]^nums[j])
        res = set()
        for i in s:
            for j in nums:
                res.add(i^j)
        return len(res)
