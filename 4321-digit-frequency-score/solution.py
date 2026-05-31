class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        res = 0
        d= {}
        for i in str(n):
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1 
        for i in d:
            res += d[i]*int(i)
        return res
    
