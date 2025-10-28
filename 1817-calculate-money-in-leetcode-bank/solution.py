class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        week = True
        s = 0
        a = 1
        for i in range(1,n+1):
            s += a
            a+=1
            if i%7 == 0:
                week = True
                monday +=1
                a = monday
            
        return s
