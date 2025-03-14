class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pilessum = sum(piles)
        low = 1
        high = max(piles)

        def check(mid,h):
            c = 0
            for i in piles:
                c += (i+mid-1)//mid
            

            if c <=h:
                return True
            return False
        # print(pilessum)
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            if check(mid,h):
                ans = min(ans,mid)
                high = mid-1
                
            else:
                low = mid+1
            
        return ans
