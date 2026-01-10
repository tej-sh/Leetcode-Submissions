class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def zero(x):
            if x <= 0:
                return 0
            return x//5+zero(x//5)
        return zero(n)
