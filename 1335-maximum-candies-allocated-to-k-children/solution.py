class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candiesum = sum(candies)
        if candiesum < k:
            return 0
        
        low = 1
        high =candiesum//k
        def check(mid,k):
            c = 0
            for i in range(len(candies)):
                c += candies[i]//mid
            
            if c >=k:
                return True
            return False

            
        ans = 0
        while low<=high:
            mid = low+ (high-low)//2
            
            if check(mid,k):
                ans = max(ans,mid)
                low = mid+1
            else:
                high = mid-1
    
        return ans
