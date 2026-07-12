class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        import math
        spent = 0
        res = k
        used = 1
        mod = 10**9 + 7
        for i in nums:
            if res < i:
                need = i - res
                t = math.ceil(need/k)
                inital = used
                final = used + t-1
                spent += (inital+final)*t//2
                res += k*t
                used += t
                
                
            res -= i

        return spent%mod
                
