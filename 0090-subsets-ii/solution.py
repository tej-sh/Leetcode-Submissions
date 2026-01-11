class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        def ans(i,l,seen):
            if i==n:
                if l[:] not in seen:
                    res.append(l[:])
                    seen.append(l[:])
                return
            l.append(nums[i])
            ans(i+1,l,seen)
            l.pop()

            ans(i+1,l,seen)
        ans(0,[],[])
        return res
