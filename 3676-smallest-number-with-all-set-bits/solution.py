class Solution:
    def smallestNumber(self, n: int) -> int:
        b = "1"*len(bin(n)[2::])
        
        return int(b,2)
