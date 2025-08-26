# import statistics
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums)//2
        val = 0
        d= {}
        for i in nums:
            if i in d:
                d[i] += 1
                if target <=d[i]:
                    val = i
                    target = d[i]
            else:
                d[i] = 1
                if target <=d[i]:
                    val = i
                    target = d[i]
                
        return val
        
