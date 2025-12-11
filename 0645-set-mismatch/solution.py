class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = set(nums)
        dupele = -1
        d = {}
        for i in nums:
            if i in d:
                dupele = i
                break
            else:
                d[i] = 0
        x = (n*(n+1)//2) - sum(dup)
        return [dupele,x]


