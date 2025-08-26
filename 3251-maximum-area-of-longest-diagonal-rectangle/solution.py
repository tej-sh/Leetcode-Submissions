class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        s = 0
        l = 0
        for i in dimensions:
            
            a = pow(i[0],2)
            b = pow(i[1],2)
            c = a+b
            if s < c: 
                s = c
                l = i[0]* i[1]

            elif s == c:
                if l < i[0]*i[1]:
                    l = i[0]*i[1]
        return l
