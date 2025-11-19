class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] != 0:
            return False
        n = len(bits)-2
        c = 0
        while n>=0 and bits[n]==1:
            c+=1
            n-=1
        return c%2 == 0
        
