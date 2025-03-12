class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        p1 =0
        p2 = 0
        ans = ""
        c = 0
        while p1 < n and p2 < n:
            if s[p1] != s[p2]:
                ans += s[p2]
                p1 = p2
            else:
                if p2 - p1 < 2:
                    ans+=s[p2]
                    
            p2+=1
        return (ans)

                
