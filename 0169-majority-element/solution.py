class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = (len(nums)//2)
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in d:
            if d[i] > target:
                return i
