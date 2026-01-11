class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def ans(i,l):
            if i>=n:
                res.append(l[::])
                return 
            l.append(nums[i])
            ans(i+1,l)
            l.pop()

            ans(i+1,l)
        ans(0,[])
        return res
            
        

            
