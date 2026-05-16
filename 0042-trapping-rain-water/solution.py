class Solution:
    def trap(self, height: List[int]) -> int:

        a = 0
        n = len(height)
        lmax = []
        rmax = [0]*n
        prev = float("-inf")
        for i in range(n):
            if height[i] > prev:
                lmax.append(height[i])
                prev = height[i]
            else:
                lmax.append(prev)
        prev = float("-inf")
        
        for i in range(n-1,-1,-1):
            
            if height[i] > prev:
                rmax[i]=height[i]
                prev = height[i]
            else:
                rmax[i]=prev
        res = 0
        for i in range(n):
            res+= min(lmax[i],rmax[i])-height[i]
        return res
