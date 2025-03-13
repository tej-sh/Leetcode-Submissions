class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def checkzero(nums,queries,mid):
            n = len(nums)
            prefix = [0]*n
            for i in range(mid):
                l,r,v = queries[i]
                prefix[l] -= v
                if r+1 < n :
                    prefix[r+1] +=v

            for i in range(1,n):
                prefix[i] += prefix[i-1]
            
            for i in range(n):
                if prefix[i]+nums[i] >0:
                    return False
            return True
    



        q = len(queries)
        low = 0
        high = q
        ans = q+1
        while low<=high:
            mid = low + (high-low)//2

            if checkzero(nums,queries,mid):
                high = mid-1
                ans = min(mid , ans)
            else:
                low = mid+1
        

        if ans>q :
            return -1
        else:
            return ans
