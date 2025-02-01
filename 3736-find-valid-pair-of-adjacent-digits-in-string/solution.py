class Solution:
    def findValidPair(self, s: str) -> str:
        fi = False
        n=len(s)
        for i in range(n-1):
            x=int(s[i])
            y=int(s[i+1])
            if s[i]!=s[i+1]:
                if s.count(s[i])==x:
                    if s.count(s[i+1])==y:
                        fi=True
                        break
        if fi:
            return s[i:i+2]
        return ""
            
