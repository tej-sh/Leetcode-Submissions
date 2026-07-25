class Solution:
    def maxProduct(self, n: int) -> int:
        from collections import defaultdict
        l = list(str(n))
        d = defaultdict(int)
        m1,m2 = -1,-1
        for i in l:
            if int(i)>m1:
                m2 = m1
                m1= int(i)
            elif int(i) >m2:
                m2 = int(i)
            d[int(i)] +=1
        if d[m1]>1:
            return m1*m1
        else:
            return m1*m2
        
