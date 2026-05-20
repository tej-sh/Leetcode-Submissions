class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        p1 = 0
        d1 = {}
        d2 = {}
        res = []
        for i in range(n):
            c = 0
            if A[i] in d1:
                d1[A[i]] +=1
            else:
                d1[A[i]] =1
            if B[i] in d2:
                d2[B[i]] +=1
            else:
                d2[B[i]] = 1
            for i in d1:
                if i in d2:
                    c+= abs(d1[i]-d2[i])+1
            res.append(c)
        return res
