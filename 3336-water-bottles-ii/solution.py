class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        if numBottles < numExchange:
            return ans
        empty = numBottles-numExchange
        empty +=1
        ans +=1
        numExchange +=1
        while empty >= numExchange:
            empty = empty - numExchange
            empty +=1
            ans+=1
            numExchange+=1
        return ans


