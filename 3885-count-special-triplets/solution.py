class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        ans = 0
        l = {}
        for i in nums:
            d[i]-=1
            if d[i] == 0:
                d.pop(i)
            target = i*2
            if target in l and target in d:
                ans += l[target]*d[target]
            
            l[i] = l.get(i,0)+1
        return ans%(10**9+7)

