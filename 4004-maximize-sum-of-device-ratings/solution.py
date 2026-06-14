class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        sm =[]
        m = []
        for i in units:
            i.sort()
            m.append(i[0])
            if len(i) >= 2:
                sm.append(i[1])
            else:
                sm.append(0)
        res = sum(m)
        mn = min(m)

        wannabe = sum(sm)

        for i in range(len(m)):
            res = max(res,mn+wannabe-sm[i])
        return res
        
            
                
