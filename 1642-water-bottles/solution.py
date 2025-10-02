class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        r1 = numBottles%numExchange  
        r2 = numBottles//numExchange
        ans += r2
        while (r1+r2) >= numExchange: 
            total = r1+r2
            ans += total//numExchange
            r1 = total%numExchange
            r2 = total//numExchange
        return ans
