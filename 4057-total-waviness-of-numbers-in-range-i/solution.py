class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1,num2+1):
            x = str(i)
            n = len(str(i)) 
            if n <=2:
                continue
            for j in range(1,n-1):
                if int(x[j-1]) < int(x[j]) and int(x[j]) > int(x[j+1]):
                    res+=1
                elif int(x[j-1]) > int(x[j]) and int(x[j]) < int(x[j+1]):
                    res+=1
        return res


