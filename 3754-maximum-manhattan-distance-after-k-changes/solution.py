class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        jk=len(s)
        northdis=[0]*(jk+1)
        westdis=[0]*(jk+1)
        eastdis=[0]*(jk+1)
        southdis=[0]*(jk+1)
        for i in range(jk):
            northdis[i+1]=northdis[i]+(1 if s[i]=='N' else 0)
            southdis[i+1]=southdis[i]+(1 if s[i]=='S' else 0)
            eastdis[i+1]=eastdis[i]+(1 if s[i]=='E' else 0)
            westdis[i+1]=westdis[i]+(1 if s[i]=='W' else 0)
        resultigg=0
        for i in range(1,jk+1):
            x=eastdis[i]-westdis[i]
            y=northdis[i]-southdis[i]
            m=abs(x)+abs(y)
            if x>0:
                px=westdis[i]
            elif x<0:
                px=eastdis[i]
            else:
                px=max(eastdis[i],westdis[i])
            if y>0:
                py=southdis[i]
            elif y<0:
                py=northdis[i]
            else:
                py=max(northdis[i],southdis[i])
            dum=2*min(k,px+py)
            cdum=min(i,m+dum)
            resultigg=max(resultigg,cdum)
        return resultigg
