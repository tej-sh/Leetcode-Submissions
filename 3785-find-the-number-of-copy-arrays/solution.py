class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        w = bounds[0][0]
        L = bounds[0][1]
        
        def check(w,L,n):
            for i in range(1,n):
                d = original[i]-original[i-1]
                w+=d
                L+=d
    
                w = max(w,bounds[i][0])
                L = min(L,bounds[i][1])
    
                if w>L:
                    return 0
    
            return L- w +1

        c = check(w,L,n)
        return c
