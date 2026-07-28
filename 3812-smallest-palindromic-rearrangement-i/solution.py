class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import defaultdict
        l = sorted(list(s))
        n = len(s)
        d = defaultdict(int)
        for i in l:
            d[i]+=1
        
        res = ""
        mid = ""

        for i in d:
            if d[i] > 1:
                if d[i]%2 == 0:
                    res+= i*(d[i]//2)
                elif mid =="":
                    res += i*(d[i]//2)
                    mid = i
            elif d[i] == 1 and mid == "":
                mid = i
        return res+mid+res[::-1]

        
