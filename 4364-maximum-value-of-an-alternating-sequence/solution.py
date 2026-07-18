class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        # res = s
        if n==1:
            return s
        res = s+(n//2)*m - ((n)//2-1)
        # else:
        #     res = s+(n//2*m)-(n)//2
        return res
        
        
        # flag = False
        # for i in range(1,n):
        #     if flag:
        #         prev = prev-1
        #         flag = False
        #     else:
        #         prev += m
        #         res = max(res,prev)
        #         flag = True
            
        # return res
