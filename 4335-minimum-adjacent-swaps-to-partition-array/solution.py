class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        res = 0
        mod = 10**9+7
        first = 0
        second = 0
        third = 0
        for i in nums:
            if i < a:
                res+= second + third
                first += 1
            elif i>=a and i<=b:
                res += third
                second+=1
            else:
                third+=1
        return res%mod
