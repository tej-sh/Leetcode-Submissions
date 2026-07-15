class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        # oddsum = sum(i for i in range(1,2*n+1) if i%2!=0 )
        # evensum = sum(i for i in range(1,2*n+1) if i%2 == 0)

        oddsum = n**2
        evensum = n*(n+1)
        return math.gcd(oddsum,evensum)
