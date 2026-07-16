class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        n = len(nums)
        x = 1
        arr = []
        for i in nums:
            x = max(i,x)
            arr.append(math.gcd(i,x))
        
        arr.sort()
        gcds = 0
        for i in range(n//2):
            gcds += math.gcd(arr[i],arr[-i-1])
        # if n%2 != 0:
        #     return gcds+arr[n//2+1]
        return gcds





