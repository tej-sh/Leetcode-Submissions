class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for i in nums:
            d[i] +=1
        
        a = sorted(d.items(),key=lambda x:x[1],reverse = True)
        res = []
        for i in range(k):
            res.append(a[i][0])
        return res

