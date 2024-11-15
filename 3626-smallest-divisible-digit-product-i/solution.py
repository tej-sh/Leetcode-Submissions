class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            j = str(i)
            product = 1
            for z in j:
                product *= int(z)
                if product%t ==0:
                    return i
            
