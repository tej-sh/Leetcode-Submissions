class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low,high+1):
            if i < 10:
                continue
            s = str(i)
            if len(s)%2 !=0:
                continue
            
            a = s[0:len(s)//2]
            b = s[len(s)//2: high+1]
            if sum(map(int,a)) == sum(map(int,b)):
                c+=1
                # print(a,b)
        return c
