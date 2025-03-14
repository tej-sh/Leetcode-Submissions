class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        diffarray = [0]*n

        for i in queries:
            l,r = i
            diffarray[l] -= 1
            if r+1 < n:
                diffarray[r+1] += 1
        
        for i in range(1,n):
            diffarray[i] += diffarray[i-1]
        
        for i in range(n):
            if diffarray[i] + nums[i] > 0:
               return False
        return True
