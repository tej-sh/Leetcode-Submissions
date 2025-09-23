class Solution:
    def countPrimes(self, n: int) -> int:
        l = [True]*(n-1)
        if n<=2:
            return 0
        for i in range(int(math.sqrt(n))+1):
            if l[i] == True:
                if i+1 ==1:
                    l[i] = False
                    continue
                temp = 2
                while (i+1)*temp <n:
                    l[(i+1)*temp-1] = False
                    temp+=1
            else:
                continue
        c = 0
        for i in l:
            if i == True:
                c+=1
        return c
        
        
