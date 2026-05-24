class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        res = []
        for i in d:
            for j in range(min(d[i],k)):
                res.append(i)
        return res
