class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in items[:k]]
