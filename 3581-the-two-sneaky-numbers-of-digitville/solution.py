class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        ans = set()
        c = 0
        for i in nums:
            if i in d:
                d[i] += 1
                ans.add(i)
                if len(ans) == 2:
                    return list(ans)
            else:
                d[i] =1 
        
