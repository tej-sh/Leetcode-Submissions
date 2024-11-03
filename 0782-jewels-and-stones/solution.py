class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count =0
        for x in jewels:
            if x in stones:
                count +=stones.count(x)
        return count
