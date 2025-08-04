class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        res = 0
        cur = 0
        for i in range(len(fruits)):
            if fruits[i] in d:
                d[fruits[i] ] +=1
                
            else:
                d[fruits[i] ] = 1
        
            while(len(d) >= 3):
                if d[fruits[cur]] > 1:
                    d[fruits[cur]] -=1
                else:
                    del d[fruits[cur]]
                cur +=1
            res= max(res,i-cur+1)
        return res
