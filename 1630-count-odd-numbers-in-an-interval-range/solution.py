class Solution:
    def countOdds(self, low: int, high: int) -> int:
        x = high-low+1
        if (x)%2 ==0:
            return x//2
        else:
            if low%2 !=0 or high%2!=0:
                return x//2+1
            else:
                return x//2
