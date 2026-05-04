class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        p = []
        n = []

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        
        p1 = 0
        p2 = 0
        while p1<len(p) and p2<len(n):
            res.append(p[p1])
            res.append(n[p1])
            p1 += 1
            p2+=1
        
        if p1<len(p):
            res.append(p[p1])
        
        if p2<len(n):
            res.append(p[p2])
        
        return res
