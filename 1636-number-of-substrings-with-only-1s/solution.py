class Solution:
    def numSub(self, s: str) -> int:
        c =0
        modulo = 10**9 + 7
        n = len(s)
        res = 0
        for i in s:
            if i == "1":
                c+=1
            else:
                res+=(c*(c+1)//2)%modulo
                c = 0
        if c:
            res+=(c*(c+1)//2)%modulo
        return res
