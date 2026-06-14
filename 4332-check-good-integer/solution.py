class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        
        sq = 0
        sm = 0
        for i in str(n):
            sq += int(i)**2
            sm += int(i)
        # print(sm,sq)
        return sq - sm >= 50
