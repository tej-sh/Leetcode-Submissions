class Solution:
    def maxDistance(self, moves: str) -> int:
        
        x = 0
        y = 0
        uc = 0
        for i in moves:
            if i =="U":
                y+=1
            elif i=="D":
                y-=1
            elif i=='L':
                x-=1
            elif i == 'R':
                x+=1
            else:
                uc +=1
        x = abs(x)
        y = abs(y)
        
        return x+y+uc
                

