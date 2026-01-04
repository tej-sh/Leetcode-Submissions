import math 
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ts = 0
        for i in nums:
            s = 0
            c = 0
            for j in range(1,int(math.sqrt(i))+1):
                if i%j==0:
                    c+=1
                    s+=j
                    if j != i//j:
                        c+=1
                        s+=i//j
                        
                if c >4:
                    break
                    
            if c==4:
                ts+=s
        return ts
            

