class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        x = sorted(list(set(arr[::])))
        # print(x)
        # x = set(x)
        n = 1
        for i in x:
            d[i] = n
            n+=1
        res = []
        # print(x)
        # print(arr)
        # print(d)
        # print(res)
        for i in arr:
            res.append(d[i])
        return res
        
