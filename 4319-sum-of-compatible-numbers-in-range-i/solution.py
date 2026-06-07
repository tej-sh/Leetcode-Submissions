class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        for i in range(1,n+k+1):
            if (abs(n-i) <=k) and ((n & i) == 0):
                res+= i
        return res
