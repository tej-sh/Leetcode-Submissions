class Solution:
    def smallestNumber(self, n: int) -> int:
        binary =bin(n)[2::]
        res = "1"*len(binary)
        return (int(res,2))
        
        
