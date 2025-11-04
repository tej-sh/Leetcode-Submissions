class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0)+1
        a = sorted(d.items(), key = lambda item: item[1] , reverse= True)
        print(a)
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return ans
