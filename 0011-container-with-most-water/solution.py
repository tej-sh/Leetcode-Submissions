class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        p1 = 0
        p2 = n-1
        ans = 0
        while p1 <p2:
            if height[p1] < height[p2]:
                
                ans =max(ans, height[p1]*(p2-p1))
                p1+=1
            else:
                
                ans =max(ans, height[p2]*(p2-p1))
                p2-=1
        return ans
