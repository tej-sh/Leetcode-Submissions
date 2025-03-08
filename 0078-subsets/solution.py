class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1<<n):
            x = []
            for j in range(n):
                if i&(1<<j):
                    x.append(nums[j])
            res.append(x)
        
        return res

