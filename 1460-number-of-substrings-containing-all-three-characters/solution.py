class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        d = {'a':-1 , 'b' : -1 , 'c':-1 }
        for i in range(n):   
            d[s[i]] = i
            if -1 not in d.values():
                c+=min(d.values())+1
        return c
