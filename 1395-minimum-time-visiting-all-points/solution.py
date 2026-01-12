class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for i in range(1, len(points)):
            x, y = points[i - 1]
            tx, ty = points[i]
            
            while x != tx or y != ty:
                if x < tx:
                    x += 1
                elif x > tx:
                    x -= 1
                
                if y < ty:
                    y += 1
                elif y > ty:
                    y -= 1
                
                time += 1
        
        return time

